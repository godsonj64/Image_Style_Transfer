from fastapi import APIRouter

from app.schemas.task_api import (
    ParseTaskRequest,
    ParseTaskResponse,
    PlanTaskRequest,
    PlanTaskResponse,
    build_parse_response,
    build_plan_response,
)

router = APIRouter(prefix="/task", tags=["tasks"])


@router.post("/parse", response_model=ParseTaskResponse)
async def parse_task(payload: ParseTaskRequest) -> ParseTaskResponse:
    return build_parse_response(payload.raw_input)


@router.post("/plan", response_model=PlanTaskResponse)
async def plan_task(payload: PlanTaskRequest) -> PlanTaskResponse:
    return build_plan_response(payload.objective)
