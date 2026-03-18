from app.orchestration.verifier import VerificationOutcome, Verifier


def test_verifier_accepts_clean_result() -> None:
    verifier = Verifier()
    result = verifier.verify(schema_ok=True, tool_success=True, semantic_ok=True)
    assert result.outcome == VerificationOutcome.accept


def test_verifier_retries_on_tool_failure() -> None:
    verifier = Verifier()
    result = verifier.verify(schema_ok=True, tool_success=False, semantic_ok=True)
    assert result.outcome == VerificationOutcome.retry_different_tool
