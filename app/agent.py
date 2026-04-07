from app.llm import call_llm
from app.mcp_client import call_tool

async def run_agent(user_input: str):

    async def run_agent(user_input: str):
    tools = await get_registered_tools()
    decision = await call_llm(f"""
    Available tools: {", ".join(tools)}
    User said: {user_input}
    Should we call a tool? If yes, return:
    TOOL:tool_name:input
    Otherwise return:
    ANSWER:response
    """)
    
    # Step 1: Ask LLM what to do
    decision = await call_llm(f"""
    User said: {user_input}
    Should we call a tool? If yes, return:
    TOOL:tool_name:input
    Otherwise return:
    ANSWER:response
    """)

    if decision.startswith("TOOL:"):
        _, tool_name, tool_input = decision.split(":", 2)
        tool_result = await call_tool(tool_name, tool_input)

        # Send result back to LLM for final response
        final = await call_llm(f"""
        Tool result: {tool_result}
        Give final user response.
        """)
        return final
    return decision.replace("ANSWER:", "")
