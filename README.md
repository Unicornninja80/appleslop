# appleslop

Daily AppleScript snippets, checked into this repo by an automated job.

## Structure

- `applescripts/` – one `.applescript` per day, named with a deterministic funny codename (e.g. `sassy-stem-sprint.applescript`).
- `scripts/generate_applescript.py` – builds a new AppleScript from a rotating template list and tags it with the codename.
- `scripts/name_utils.py` – helper for generating the codename + slug.
- `scripts/daily_apple_commit.sh` – pulls the latest repo, generates today’s script (if missing), and pushes the commit.

## Local testing

```bash
cd appleslop
python3 scripts/generate_applescript.py --date 2026-02-14 --out applescripts/test.applescript
./scripts/daily_apple_commit.sh
```

The cron job calls the same shell script every morning.
