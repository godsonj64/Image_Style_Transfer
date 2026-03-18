# Agent Desktop Scaffold

This folder contains a production-oriented backend foundation for the local-first desktop agent blueprint.

## Included

- FastAPI app factory with startup lifecycle and `/health`, `/task/parse`, `/task/plan` routes.
- Typed schemas for task graphs and API payloads.
- Tool protocol + registry abstractions.
- Policy engine, verifier, reward engine, and node state machine.
- SQLAlchemy persistence models, DB initializer, and transaction session helper.
- Structured JSON logging setup.
- Unit + integration tests.
- Packaging scripts for creating downloadable artifacts.

## Run locally

```bash
cd agent-desktop/backend
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
uvicorn app.main:app --reload
```

## Build downloadable artifacts

```bash
cd agent-desktop/backend

# Source bundle (developer-oriented)
./scripts/package_backend.sh

# Run-ready bundle (end-user oriented)
./scripts/build_run_ready_bundle.sh
./scripts/verify_bundle.sh
# output: agent-desktop/backend/dist/agent-desktop-backend-run-ready.tar.gz
```

## Run-ready bundle usage

After downloading and extracting `agent-desktop-backend-run-ready.tar.gz`:

```bash
cd agent-desktop-backend
./run_backend.sh
```

The launcher script creates a local virtual environment, installs dependencies, and starts the API on `http://127.0.0.1:8000`.
