from fastapi import FastAPI, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.agent import run_agent

app = FastAPI(title="AI Agent API")

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat with the AI Agent.

    **Sample Request**
    ```json
    {
      "message": "What is the weather in Bengaluru?"
    }
    ```

    **Sample Response**
    ```json
    {
      "response": "It’s sunny and 32°C in Bengaluru."
    }
    ```
    """
    try:
        response = await run_agent(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        # Show exact error in UI
        raise HTTPException(status_code=500, detail=str(e))