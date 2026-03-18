from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class NodeType(str, Enum):
    intent = "intent"
    retrieval = "retrieval"
    skill = "skill"
    planner = "planner"
    tool = "tool"
    validator = "validator"
    approval = "approval"
    artifact = "artifact"
    memory_update = "memory_update"
    reward_update = "reward_update"
    stop = "stop"


class NodeState(str, Enum):
    pending = "pending"
    ready = "ready"
    running = "running"
    blocked = "blocked"
    waiting_approval = "waiting_approval"
    verifying = "verifying"
    failed = "failed"
    succeeded = "succeeded"
    rolled_back = "rolled_back"
    skipped = "skipped"


class TaskNode(BaseModel):
    id: str
    label: str
    node_type: NodeType
    objective: str
    dependencies: list[str] = Field(default_factory=list)
    state: NodeState = NodeState.pending
    tool_name: str | None = None
    validator_name: str | None = None


class TaskEdge(BaseModel):
    source: str
    target: str


class TaskGraph(BaseModel):
    id: str
    session_id: str
    version: int = 1
    created_at: datetime
    nodes: list[TaskNode] = Field(default_factory=list)
    edges: list[TaskEdge] = Field(default_factory=list)
