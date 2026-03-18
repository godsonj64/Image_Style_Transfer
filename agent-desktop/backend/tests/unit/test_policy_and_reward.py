from app.orchestration.policy import PolicyDecision, PolicyEngine
from app.orchestration.reward_engine import RewardEngine, RewardInput


def test_policy_requires_approval_for_high_risk_tools() -> None:
    engine = PolicyEngine()
    assert engine.decide("run_shell_guarded") == PolicyDecision.approval_required


def test_reward_engine_formula() -> None:
    engine = RewardEngine()
    score = engine.compute(
        RewardInput(
            success=1,
            retries=1,
            manual_repair=0,
            approval_interruptions=1,
            normalized_latency=0.5,
            user_approved=1,
        )
    )
    assert score == 1.95
