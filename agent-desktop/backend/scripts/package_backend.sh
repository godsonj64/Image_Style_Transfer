#!/usr/bin/env bash
set -euo pipefail

BACKEND_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT_DIR="$(cd "$BACKEND_DIR/.." && pwd)"
DIST_DIR="$BACKEND_DIR/dist"
ARTIFACT="$DIST_DIR/agent-desktop-backend.tar.gz"

mkdir -p "$DIST_DIR"

tar \
  --exclude='__pycache__' \
  --exclude='.pytest_cache' \
  -czf "$ARTIFACT" \
  -C "$BACKEND_DIR" app pyproject.toml scripts \
  -C "$ROOT_DIR" README.md

echo "Created backend artifact: $ARTIFACT"
