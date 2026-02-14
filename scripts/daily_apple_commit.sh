#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

git pull --rebase || true

DATE_UTC=${DATE_OVERRIDE:-$(date -u +%Y-%m-%d)}

mapfile -t NAME_PARTS < <(DATE_VALUE="$DATE_UTC" python3 - <<'PY'
import datetime as dt
import os
from scripts.name_utils import funny_name, funny_slug

value = os.environ["DATE_VALUE"]
seed = int(dt.date.fromisoformat(value).strftime("%Y%m%d"))
print(funny_name(seed))
print(funny_slug(seed))
PY
)

FUNNY_NAME="${NAME_PARTS[0]}"
FUNNY_SLUG="${NAME_PARTS[1]}"
OUTPUT_FILE="applescripts/${FUNNY_SLUG}.applescript"

if [[ -f "$OUTPUT_FILE" ]]; then
  echo "AppleScript for $DATE_UTC (aka $FUNNY_NAME) already exists."
else
  python3 scripts/generate_applescript.py --date "$DATE_UTC" --out "$OUTPUT_FILE"
  echo "Created $OUTPUT_FILE for $FUNNY_NAME"
fi

if git status --short | grep -q "applescripts"; then
  git add "$OUTPUT_FILE"
  git commit -m "Add AppleScript (${FUNNY_NAME})"
  git push origin main
else
  echo "No changes to commit."
fi
