"""LangServe entry point for Email Manager graph."""
from fastapi import FastAPI
from langserve import add_routes
from .graph import email_manager_graph

app = FastAPI(
    title="Patience – Email Manager",
    version="0.1.0",
    description="LangGraph server exposing the Email Communication Manager graph.",
)

add_routes(
    app,
    email_manager_graph,
    path="/graph",
    enable_public_stream=True,
)

@app.get("/")
async def root():
    return {"msg": "Patience Email Manager up"}
