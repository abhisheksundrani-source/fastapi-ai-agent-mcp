from pydantic import BaseModel
from typing import Any, Dict

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

class ToolRequest(BaseModel):
    tool: str
    input: str

class ToolResponse(BaseModel):
    result: Dict[str, Any]