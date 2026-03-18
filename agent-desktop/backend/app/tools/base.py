from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True)
class ToolContext:
    session_id: str
    workspace_root: str


@dataclass(slots=True)
class PrecheckResult:
    ok: bool
    reason: str | None = None


@dataclass(slots=True)
class ToolResult:
    success: bool
    payload: dict


@dataclass(slots=True)
class RollbackResult:
    success: bool
    details: str | None = None


class Tool(Protocol):
    name: str
    risk_class: str
    input_schema: dict
    output_schema: dict

    async def precheck(self, ctx: ToolContext, args: dict) -> PrecheckResult: ...

    async def execute(self, ctx: ToolContext, args: dict) -> ToolResult: ...

    async def rollback(self, ctx: ToolContext, args: dict, result: dict | None) -> RollbackResult: ...
