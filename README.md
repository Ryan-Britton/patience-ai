# Patience‑AI – Email Manager Vertical Slice

This repository is the **MVP scaffold** for Patience‑AI, starting with the *Email Communication Manager* vertical slice.

## Stack
| Layer | Tech |
|-------|------|
| Agent orchestration | **Python + LangChain / LangGraph** |
| API server & dev loop | **LangServe** (FastAPI) |
| Vector memory (30‑day TTL) | **Weaviate** |
| Knowledge‑graph memory | **Graphiti MCP → Neo4j** |
| Integrations | **n8n** (Docker) |
| LLM embeddings (optional local) | **Ollama** |

## Quick start (local dev)

1.  Copy `.env.example` to `.env` and fill in secrets.  
2.  `docker compose up -d` – spins Weaviate, Neo4j + Graphiti MCP, n8n, and the **LangServe** hot‑reload container.  
3.  Open `http://localhost:8000/chat` – LangGraph Chat UI connected to the local graph.  
4.  Import the workflow under `workflows/email_manager_demo.json` into your local n8n instance (`http://localhost:5678`).  
5.  Send a test email to **ryan.michael.britton@outlook.com**, or manually trigger the webhook inside n8n.  
6.  Observe traces in **LangSmith** (make sure your API key is in `.env`).  
7.  Edit code in `apps/email_manager/graph.py`; the container auto‑reloads (thanks to `--reload`).  

## Deploy to LangGraph Platform

GitHub Action **.github/workflows/deploy.yml** builds this same container and runs  
`langgraph deploy --project=staging --env=.env.staging`.

Promote to prod from the LangGraph UI when staging is green.

---
### Repo layout

```
apps/
  email_manager/        # the first graph
infra/
  docker-compose.yml    # full local stack
workflows/
  email_manager_demo.json
.env.example            # template for secrets
requirements.txt
```
