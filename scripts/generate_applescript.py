#!/usr/bin/env python3
"""Generate a daily AppleScript file with some variety."""

from __future__ import annotations

import argparse
import datetime as dt
import random
import textwrap
from pathlib import Path

TEMPLATES = [
    {
        "title": "Focus Playlist Booster",
        "body": textwrap.dedent(
            """
            -- Title: Focus Playlist Booster
            -- Generated on {date_str}
            set targetPlaylist to "{playlist_name}"
            tell application "Music"
                activate
                if exists playlist targetPlaylist then
                    set shuffle enabled to true
                    set songRepeat to all
                    play playlist targetPlaylist
                else
                    display dialog "Create a playlist called '" & targetPlaylist & "' for this automation to shine." buttons {"Noted"}
                end if
            end tell
            """
        ),
    },
    {
        "title": "Reminder Sprint",
        "body": textwrap.dedent(
            """
            -- Title: Reminder Sprint
            -- Generated on {date_str}
            set reminderTitle to "{reminder_title}"
            set reminderNotes to "{reminder_note}"
            tell application "Reminders"
                activate
                make new reminder with properties {{name:reminderTitle, body:reminderNotes, remind me date:(current date) + ({offset_hours} * hours)}}
            end tell
            """
        ),
    },
    {
        "title": "Note Capsule",
        "body": textwrap.dedent(
            """
            -- Title: Note Capsule
            -- Generated on {date_str}
            set noteHeadline to "{note_headline}"
            set noteBody to "{note_body}"
            tell application "Notes"
                activate
                set targetFolder to first folder whose name is "Notes"
                make new note at targetFolder with properties {{name:noteHeadline, body:noteHeadline & "\n\n" & noteBody}}
            end tell
            """
        ),
    },
    {
        "title": "Desktop Snapshot",
        "body": textwrap.dedent(
            """
            -- Title: Desktop Snapshot
            -- Generated on {date_str}
            set desktopPath to POSIX path of (path to desktop folder)
            set archiveFolder to desktopPath & "Snapshots"
            do shell script "mkdir -p '" & archiveFolder & "'"
            set stamp to do shell script "date +%Y%m%d-%H%M%S"
            set archiveFile to archiveFolder & "/Workspace-" & stamp & ".png"
            do shell script "screencapture -x '" & archiveFile & "'"
            display notification "Saved screenshot " & archiveFile with title "Desktop Snapshot"
            """
        ),
    },
    {
        "title": "Window Layout Reset",
        "body": textwrap.dedent(
            """
            -- Title: Window Layout Reset
            -- Generated on {date_str}
            set windowBounds to {{ {left}, {top}, {right}, {bottom} }}
            tell application "Finder"
                activate
                set bounds of front window to windowBounds
                set current view of front window to list view
            end tell
            """
        ),
    },
]

PLAYLISTS = [
    "Morning Synth",
    "Coffee Shop Logic",
    "Deep Focus",
    "Lo-Fi Momentum",
    "Rev Up"
]

REMINDER_TITLES = [
    "Micro stretch break",
    "Send quick gratitude note",
    "Inbox zero sprint",
    "Hydration check",
]

REMINDER_NOTES = [
    "Two-minute reset: breathe in for 4, out for 6.",
    "Ping a teammate with a thank-you.",
    "Skim starred emails only—no rabbit holes.",
    "Walk around while a stopwatch counts 120 seconds.",
]

NOTE_HEADLINES = [
    "Idea fragments",
    "Debug diary",
    "Song sketches",
    "Random sparks",
]

NOTE_BODIES = [
    "Capture three bullet points about whatever is top-of-mind.",
    "List one lesson learned from today.",
    "Brain-dump any lingering thoughts before sleep.",
    "Imagine a headline describing your next win.",
]


def build_script(date: dt.date) -> str:
    seed = int(date.strftime("%Y%m%d"))
    random.seed(seed)
    template = random.choice(TEMPLATES)
    params = {
        "date_str": date.isoformat(),
        "playlist_name": random.choice(PLAYLISTS),
        "reminder_title": random.choice(REMINDER_TITLES),
        "reminder_note": random.choice(REMINDER_NOTES),
        "offset_hours": random.choice([0.5, 1, 2, 3]),
        "note_headline": random.choice(NOTE_HEADLINES),
        "note_body": random.choice(NOTE_BODIES),
        "left": random.randint(50, 200),
        "top": random.randint(40, 120),
        "right": random.randint(1024, 1440),
        "bottom": random.randint(700, 900),
    }
    return template["body"].format(**params).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a deterministic AppleScript for a date.")
    parser.add_argument("--date", help="Date in YYYY-MM-DD (defaults to today)")
    parser.add_argument("--out", required=True, help="Output path for the .applescript file")
    args = parser.parse_args()

    if args.date:
        target_date = dt.date.fromisoformat(args.date)
    else:
        target_date = dt.date.today()

    script_text = build_script(target_date)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(script_text, encoding="utf-8")


if __name__ == "__main__":
    main()
