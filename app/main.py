from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.agent import run_agent

app = FastAPI(title="AI Agent API")

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = await run_agent(request.message)
    return ChatResponse(response=response)