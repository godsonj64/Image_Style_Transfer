#!/usr/bin/env bash
set -euo pipefail

BACKEND_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT_DIR="$(cd "$BACKEND_DIR/.." && pwd)"
DIST_DIR="$BACKEND_DIR/dist"
STAGE_DIR="$DIST_DIR/run-ready/agent-desktop-backend"
BUNDLE_PATH="$DIST_DIR/agent-desktop-backend-run-ready.tar.gz"

rm -rf "$DIST_DIR/run-ready"
mkdir -p "$STAGE_DIR"

cp -R "$BACKEND_DIR/app" "$STAGE_DIR/app"
cp "$BACKEND_DIR/pyproject.toml" "$STAGE_DIR/pyproject.toml"
cp "$ROOT_DIR/README.md" "$STAGE_DIR/README.md"

cat > "$STAGE_DIR/.env.example" <<'ENV'
AGENT_DESKTOP_ENVIRONMENT=prod
AGENT_DESKTOP_DATA_DIR=./data
AGENT_DESKTOP_SQLITE_FILENAME=app.db
ENV

cat > "$STAGE_DIR/run_backend.sh" <<'RUN'
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

if [[ ! -d "$VENV_DIR" ]]; then
  python3 -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"
python -m pip install --upgrade pip >/dev/null
python -m pip install . >/dev/null

exec uvicorn app.main:app --host 127.0.0.1 --port 8000
RUN

cat > "$STAGE_DIR/STOP.md" <<'TXT'
To stop the backend server, press Ctrl+C in the terminal where `run_backend.sh` is running.
TXT

chmod +x "$STAGE_DIR/run_backend.sh"

tar \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  -czf "$BUNDLE_PATH" \
  -C "$DIST_DIR/run-ready" agent-desktop-backend

printf 'Run-ready bundle created: %s\n' "$BUNDLE_PATH"
printf 'Start command after extraction: ./agent-desktop-backend/run_backend.sh\n'
