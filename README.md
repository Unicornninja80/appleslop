# appleslop

Daily AppleScript snippets, checked into this repo by an automated job.

## Structure

- `applescripts/` – one `.applescript` file per day.
- `scripts/generate_applescript.py` – builds a new AppleScript from a rotating template list.
- `scripts/daily_apple_commit.sh` – pulls the latest repo, generates today’s script (if missing), and pushes the commit.

## Local testing

```bash
cd appleslop
python3 scripts/generate_applescript.py --date 2026-02-14 --out applescripts/test.applescript
```

Then run the shell script to verify end-to-end:

```bash
./scripts/daily_apple_commit.sh --dry-run
```

(The cron job calls the same script every morning.)
