import pytest
from app.agent import run_agent

@pytest.mark.asyncio
async def test_run_agent_answer():
    response = await run_agent("Hello!")
    assert "Hello" in response or "Hi" in response

@pytest.mark.asyncio
async def test_run_agent_tool(monkeypatch):
    async def mock_call_tool(tool_name, tool_input):
        return {"result": "Sunny, 32°C"}
    monkeypatch.setattr("app.mcp_client.call_tool", mock_call_tool)

    response = await run_agent("What's the weather?")
    assert "Sunny" in response
