"""LangGraph definition for the Email Communication Manager.

*This is an MVP stub – flesh out classify_email and update_categories.*
"""
import os
from langgraph.graph import StateGraph
from langchain.schema import RunnableConfig
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.tools import StructuredTool
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    temperature=0,
    model_name=os.getenv("OPENAI_MODEL", "gpt-4o-mini")
)

CLASSIFY_PROMPT = PromptTemplate.from_template(
    """You are an email classifier. 
    Given the **raw email text** delimited by <email></email>, output a JSON object:
      {{
        "persona": "Work|Personal|Family",
        "type": "Marketing|Notification|Alert|Conversation|Information|Record"
      }}
    <email>{email}</email>"""
)

def classify_email(email: str, cfg: RunnableConfig | None = None) -> dict:
    """Call LLM to classify the email."""
    prompt = CLASSIFY_PROMPT.format(email=email[:15000])
    resp = llm.invoke(prompt, config=cfg)
    import json, re
    json_str = re.search(r"\{.*\}", resp).group(0)
    return json.loads(json_str)

classify_tool = StructuredTool.from_function(
    func=classify_email,
    name="classify_email",
    description="Classify incoming email by persona and type"
)

def noop_tool(data, cfg=None):
    return data

update_categories_tool = StructuredTool.from_function(
    func=noop_tool,
    name="update_categories",
    description="Stub – calls n8n webhook to patch Outlook categories"
)

memory_tool = StructuredTool.from_function(
    func=noop_tool,
    name="write_memory",
    description="Stub – writes embeddings to Weaviate/Graphiti with TTL"
)

# --- Graph wiring ---
g = StateGraph()
g.add_node("classify", classify_tool)
g.add_node("update_labels", update_categories_tool)
g.add_node("memory", memory_tool)

# edges
g.add_edge("classify", "update_labels")
g.add_edge("update_labels", "memory")
g.add_edge("memory", "END")

email_manager_graph = g.compile()
"""
Expose email_manager_graph for import into LangServe
"""