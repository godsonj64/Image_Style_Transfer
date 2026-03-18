from dataclasses import dataclass
from enum import Enum


class VerificationOutcome(str, Enum):
    accept = "accept"
    retry_same = "retry_same"
    retry_different_tool = "retry_different_tool"
    replan = "replan"
    escalate_to_user = "escalate_to_user"
    rollback = "rollback"


@dataclass(slots=True)
class VerificationResult:
    outcome: VerificationOutcome
    reasons: list[str]


class Verifier:
    def verify(self, *, schema_ok: bool, tool_success: bool, semantic_ok: bool) -> VerificationResult:
        reasons: list[str] = []
        if not schema_ok:
            reasons.append("schema_validation_failed")
        if not tool_success:
            reasons.append("tool_runtime_failed")
        if not semantic_ok:
            reasons.append("semantic_validation_failed")

        if not reasons:
            return VerificationResult(outcome=VerificationOutcome.accept, reasons=[])

        if "tool_runtime_failed" in reasons:
            return VerificationResult(outcome=VerificationOutcome.retry_different_tool, reasons=reasons)
        if "schema_validation_failed" in reasons:
            return VerificationResult(outcome=VerificationOutcome.retry_same, reasons=reasons)
        return VerificationResult(outcome=VerificationOutcome.escalate_to_user, reasons=reasons)
