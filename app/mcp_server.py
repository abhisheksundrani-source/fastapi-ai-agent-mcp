# app/mcp_server.py
from fastapi import FastAPI, Request

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
    return {"tools": list(tools.keys())}

@app.post("/mcp")
async def call_tool(request: Request):
    data = await request.json()
    tool_name = data.get("tool")
    tool_input = data.get("input")

    if tool_name not in tools:
        return {"error": f"Tool '{tool_name}' not found"}

    result = await tools[tool_name](tool_input)
    return {"result": result}
