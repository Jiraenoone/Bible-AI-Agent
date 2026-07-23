"""FastAPI application entrypoint for Bible AI Agent."""

from fastapi import FastAPI

app = FastAPI(
    title="Bible AI Agent API",
    description="RAG-powered Bible Q&A and Search Agent",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "status": "Bible AI Agent Running 🚀",
        "version": "0.1.0",
    }