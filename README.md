#FastAPI AI Agent MCP

An AI Agent API built with FastAPI that integrates OpenAI LLMs and MCP (Model Context Protocol) tools.
The agent decides whether to answer directly or call an external tool, processes results, and returns a final response.

---

##🚀 Flow
- User Input → Sent to /chat endpoint.
- Decision Phase → LLM (gpt-4o-mini) decides:
- ANSWER:response → Direct answer.
- TOOL:tool_name:input → Calls external tool.
- Tool Execution → MCP client executes tool via HTTP.
- Finalization → LLM refines tool output into user-facing response.
- Response → Returned as JSON.

---

##🎲 Randomness
- Temperature: 0.2
- Low randomness → deterministic, concise, and reliable responses.
- Ensures consistent tool invocation decisions.

---

##🧠 Model in Use
- OpenAI GPT-4o-mini
- Optimized for speed and cost.
- Used for both decision-making and final response generation.

---

##🏗️ Architecture
```
FastAPI (REST API)
   │
   ├── /chat endpoint
   │       │
   │       └── run_agent()
   │              │
   │              ├── call_llm() → Decision
   │              │
   │              ├── call_tool() → MCP tool execution
   │              │
   │              └── call_llm() → Final response
   │
   └── JSON Response → ChatResponse
```

- FastAPI → API layer
- AsyncOpenAI → LLM client
- httpx.AsyncClient → MCP tool calls
- Schemas → Request/Response validation

---

##📦 Tech Stack & Libraries
- FastAPI → API framework
- OpenAI Python SDK → LLM integration
- httpx → Async HTTP client
- Pydantic → Data validation
- Python 3.10+ → Async/await support

---

##🔧 Scope of Improvements
- Add memory/context persistence (conversation history).
- Support multiple tools orchestration.
- Implement error handling & retries for MCP calls.
- Add logging & monitoring (Prometheus/Grafana).
- Extend with authentication & rate limiting.
- Deploy with Docker/Kubernetes for scalability.

---

##📖 Example Usage
Request
```http
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the weather in Bengaluru?"}'
```

Possible Response
```json
{
  "response": "The weather in Bengaluru is 32°C with scattered clouds."
}
```

---

##📌 Summary
This project demonstrates:
- LLM-driven decision-making (answer vs tool call).
- MCP integration for external tool execution.
- FastAPI-based API for serving responses.
- Low randomness for predictable outputs.
- Extensible architecture with clear improvement scope.
