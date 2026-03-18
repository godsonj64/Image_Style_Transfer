from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field

from app.schemas.task import NodeState, NodeType


class ParseTaskRequest(BaseModel):
    session_id: str
    raw_input: str = Field(min_length=3)


class ParseTaskResponse(BaseModel):
    request_id: str
    parsed_goal: str
    risk_class: str


class PlanTaskRequest(BaseModel):
    session_id: str
    request_id: str
    objective: str


class PlannedNode(BaseModel):
    id: str
    label: str
    node_type: NodeType
    state: NodeState
    objective: str


class PlanTaskResponse(BaseModel):
    graph_id: str
    created_at: datetime
    nodes: list[PlannedNode]


def build_parse_response(raw_input: str) -> ParseTaskResponse:
    risk_class = "medium" if "delete" in raw_input.lower() else "low"
    return ParseTaskResponse(request_id=str(uuid4()), parsed_goal=raw_input.strip(), risk_class=risk_class)


def build_plan_response(objective: str) -> PlanTaskResponse:
    return PlanTaskResponse(
        graph_id=str(uuid4()),
        created_at=datetime.now(timezone.utc),
        nodes=[
            PlannedNode(
                id=str(uuid4()),
                label="Plan task",
                node_type=NodeType.planner,
                state=NodeState.ready,
                objective=objective,
            ),
            PlannedNode(
                id=str(uuid4()),
                label="Stop",
                node_type=NodeType.stop,
                state=NodeState.pending,
                objective="Mark task complete",
            ),
        ],
    )
