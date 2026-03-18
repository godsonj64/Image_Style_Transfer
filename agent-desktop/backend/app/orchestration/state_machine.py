from __future__ import annotations

from app.schemas.task import NodeState


_ALLOWED_TRANSITIONS: dict[NodeState, set[NodeState]] = {
    NodeState.pending: {NodeState.ready, NodeState.skipped},
    NodeState.ready: {NodeState.running, NodeState.blocked, NodeState.waiting_approval, NodeState.skipped},
    NodeState.running: {NodeState.verifying, NodeState.failed, NodeState.rolled_back},
    NodeState.blocked: {NodeState.ready, NodeState.failed},
    NodeState.waiting_approval: {NodeState.ready, NodeState.failed},
    NodeState.verifying: {NodeState.succeeded, NodeState.failed, NodeState.rolled_back},
    NodeState.failed: {NodeState.ready, NodeState.skipped},
    NodeState.succeeded: set(),
    NodeState.rolled_back: {NodeState.ready, NodeState.failed},
    NodeState.skipped: set(),
}


class InvalidNodeTransition(ValueError):
    pass


class TaskNodeStateMachine:
    def can_transition(self, current: NodeState, target: NodeState) -> bool:
        return target in _ALLOWED_TRANSITIONS[current]

    def transition(self, current: NodeState, target: NodeState) -> NodeState:
        if not self.can_transition(current, target):
            raise InvalidNodeTransition(f"Invalid transition: {current.value} -> {target.value}")
        return target
