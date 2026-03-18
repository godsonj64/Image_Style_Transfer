#!/usr/bin/env bash
set -euo pipefail

BACKEND_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUNDLE_PATH="$BACKEND_DIR/dist/agent-desktop-backend-run-ready.tar.gz"

if [[ ! -f "$BUNDLE_PATH" ]]; then
  echo "Bundle missing: $BUNDLE_PATH" >&2
  exit 1
fi

tar -tzf "$BUNDLE_PATH" >/dev/null

echo "Bundle archive is readable: $BUNDLE_PATH"
