from pydantic import BaseModel


class ToolCallRequest(BaseModel):
    tool_name: str
    args: dict


class ToolCallResult(BaseModel):
    success: bool
    result: dict
    latency_ms: int
