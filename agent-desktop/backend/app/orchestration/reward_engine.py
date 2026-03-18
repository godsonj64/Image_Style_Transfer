from dataclasses import dataclass


@dataclass(slots=True)
class RewardInput:
    success: float
    retries: float
    manual_repair: float
    approval_interruptions: float
    normalized_latency: float
    user_approved: float


class RewardEngine:
    def compute(self, value: RewardInput) -> float:
        return (
            1.5 * value.success
            - 0.3 * value.retries
            - 0.8 * value.manual_repair
            - 0.2 * value.approval_interruptions
            - 0.1 * value.normalized_latency
            + 1.0 * value.user_approved
        )
