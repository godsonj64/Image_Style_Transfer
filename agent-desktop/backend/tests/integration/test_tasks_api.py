from fastapi.testclient import TestClient

from app.main import create_app


def test_parse_and_plan_endpoints() -> None:
    client = TestClient(create_app())

    parse_resp = client.post("/task/parse", json={"session_id": "s1", "raw_input": "Summarize PDFs"})
    assert parse_resp.status_code == 200
    parse_data = parse_resp.json()
    assert parse_data["parsed_goal"] == "Summarize PDFs"

    plan_resp = client.post(
        "/task/plan",
        json={"session_id": "s1", "request_id": parse_data["request_id"], "objective": "Summarize PDFs"},
    )
    assert plan_resp.status_code == 200
    plan_data = plan_resp.json()
    assert len(plan_data["nodes"]) == 2
