import httpx

async def call_tool(tool_name: str, tool_input: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8001/mcp",
            json={
                "tool": tool_name,
                "input": tool_input
            }
        )
        return response.json()