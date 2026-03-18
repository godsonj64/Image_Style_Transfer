import pytest

from app.orchestration.state_machine import InvalidNodeTransition, TaskNodeStateMachine
from app.schemas.task import NodeState


def test_state_machine_allows_valid_transition() -> None:
    machine = TaskNodeStateMachine()
    assert machine.transition(NodeState.pending, NodeState.ready) == NodeState.ready


def test_state_machine_rejects_invalid_transition() -> None:
    machine = TaskNodeStateMachine()
    with pytest.raises(InvalidNodeTransition):
        machine.transition(NodeState.pending, NodeState.running)
