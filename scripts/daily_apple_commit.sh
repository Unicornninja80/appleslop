#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

git pull --rebase

DATE_UTC=${DATE_OVERRIDE:-$(date -u +%Y-%m-%d)}
OUTPUT_FILE="applescripts/applescript-${DATE_UTC}.applescript"

if [[ -f "$OUTPUT_FILE" ]]; then
  echo "AppleScript for $DATE_UTC already exists."
else
  python3 scripts/generate_applescript.py --date "$DATE_UTC" --out "$OUTPUT_FILE"
  echo "Created $OUTPUT_FILE"
fi

if git status --short | grep -q "applescripts"; then
  git add "$OUTPUT_FILE"
  git commit -m "Add AppleScript for $DATE_UTC"
  git push origin main
else
  echo "No changes to commit."
fi
