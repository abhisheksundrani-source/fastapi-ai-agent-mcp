# app/mcp_server.py
from fastapi import FastAPI, Request
from app.schemas import ToolRequest, ToolResponse
app = FastAPI(title="MCP Server")

tools = {}

def register_tool(name: str, func: callable):
    tools[name] = func

# Example tool: weather
async def get_weather(location: str):
    return {"location": location, "forecast": "Sunny, 32°C"}

register_tool("weather", get_weather)

@app.get("/tools")
async def list_tools():
    """List all registered tools."""
    return {"tools": list(tools.keys())}

@app.post("/mcp", response_model=ToolResponse)
async def call_tool(request: ToolRequest):
    """Call a registered tool by name.
    
    **Sample Request**
    ```json
    {
      "tool": "weather",
      "input": "Bengaluru"
    }
    ```
    **Sample Response**
    ```json
    {
      "result": {
        "location": "Bengaluru",
        "forecast": "Sunny, 32°C"
      }
    }
    ```
    """
    if request.tool not in tools:
        return {"result": {"error": f"Tool '{request.tool}' not found"}}
    result = await tools[request.tool](request.input)
    return {"result": result}