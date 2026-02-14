#!/usr/bin/env python3
"""Generate a daily AppleScript file centered on Apple productivity workflows."""

from __future__ import annotations

import argparse
import datetime as dt
import random
import textwrap
from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.name_utils import funny_name

TEMPLATES = [
    {
        "title": "Dark Mode Flip",
        "body": textwrap.dedent(
            """
            -- Title: Dark Mode Flip
            -- Generated on {date_str}
            -- Codename: {codename}
            tell application "System Events"
                tell appearance preferences
                    set dark mode to not dark mode
                end tell
            end tell
            display notification "Dark mode toggled." with title "{codename}"
            """
        ),
    },
    {
        "title": "Audio Route Snap",
        "body": textwrap.dedent(
            """
            -- Title: Audio Route Snap
            -- Generated on {date_str}
            -- Codename: {codename}
            set targetDevice to "{audio_device}"
            do shell script "SwitchAudioSource -s '" & targetDevice & "'" -- requires https://github.com/deweller/switchaudio-osx
            display notification "Sound routed to " & targetDevice with title "{codename}"
            """
        ),
    },
    {
        "title": "Display Resolution Dial",
        "body": textwrap.dedent(
            """
            -- Title: Display Resolution Dial
            -- Generated on {date_str}
            -- Codename: {codename}
            set targetResolution to "{resolution}"
            do shell script "/usr/bin/defaults write /Library/Preferences/com.apple.windowserver DisplayResolutionEnabled -bool true"
            display dialog "Switch to " & targetResolution & " via Display menu" buttons {"Done"}
            """
        ),
    },
    {
        "title": "Reminders Momentum",
        "body": textwrap.dedent(
            """
            -- Title: Reminders Momentum
            -- Generated on {date_str}
            -- Codename: {codename}
            set reminderTitle to "{reminder_title}"
            set reminderNotes to "{reminder_note}"
            set dueDate to (current date) + ({offset_hours} * hours)
            tell application "Reminders"
                activate
                make new reminder with properties {{name:reminderTitle, body:reminderNotes, remind me date:dueDate}}
            end tell
            """
        ),
    },
    {
        "title": "Notes Brain Dump",
        "body": textwrap.dedent(
            """
            -- Title: Notes Brain Dump
            -- Generated on {date_str}
            -- Codename: {codename}
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
        "title": "Drafts Lightning Shot",
        "body": textwrap.dedent(
            """
            -- Title: Drafts Lightning Shot
            -- Generated on {date_str}
            -- Codename: {codename}
            set draftText to "{draft_prompt}" & "\n\n" & (do shell script "date")
            tell application "Drafts"
                activate
                create draft with text draftText
            end tell
            """
        ),
    },
    {
        "title": "Finder Desktop Sweep",
        "body": textwrap.dedent(
            """
            -- Title: Finder Desktop Sweep
            -- Generated on {date_str}
            -- Codename: {codename}
            set archiveFolder to (path to documents folder as text) & "Sorted Desktop"
            tell application "Finder"
                if not (exists folder archiveFolder) then
                    make new folder at (path to documents folder) with properties {{name:"Sorted Desktop"}}
                end if
                set desktopItems to every item of desktop
                repeat with anItem in desktopItems
                    move anItem to folder archiveFolder
                end repeat
            end tell
            display notification "Desktop cleared to Sorted Desktop" with title "{codename}"
            """
        ),
    },
    {
        "title": "Focus Status Toggle",
        "body": textwrap.dedent(
            """
            -- Title: Focus Status Toggle
            -- Generated on {date_str}
            -- Codename: {codename}
            do shell script "defaults -currentHost write com.apple.controlcenter 'NSStatusItem Visible DoNotDisturb' -bool true"
            do shell script "launchctl stop com.apple.notificationcenterui && launchctl start com.apple.notificationcenterui"
            display dialog "Focus mode nudged. Toggle via Control Center." buttons {"Nice"}
            """
        ),
    },
]

AUDIO_DEVICES = [
    "MacBook Pro Speakers",
    "AirPods Pro",
    "External Monitor",
]

RESOLUTIONS = [
    "More Space",
    "Default",
    "Larger Text",
]

REMINDER_TITLES = [
    "Inbox zero sprint",
    "Mini review session",
    "Call-back block",
    "Hydration break",
]

REMINDER_NOTES = [
    "Process flagged emails only.",
    "Brainstorm tomorrow's top 3 priorities.",
    "Send status update to the team.",
    "Fill out weekly highlights.",
]

NOTE_HEADLINES = [
    "Idea fragments",
    "Meeting crumbs",
    "Debug diary",
    "Velocity log",
]

NOTE_BODIES = [
    "Capture three bullet points about what's buzzing.",
    "List what should be delegated this week.",
    "Write one win and one lesson learned.",
    "Sketch the outline for a potential post.",
]

DRAFT_PROMPTS = [
    "What is the quickest automation you could ship today?",
    "Write a haiku about toggling dark mode.",
    "Capture a rant about context switching.",
    "List five shortcuts you rely on in Finder.",
]


def build_script(date: dt.date) -> str:
    seed = int(date.strftime("%Y%m%d"))
    random.seed(seed)
    template = random.choice(TEMPLATES)
    codename = funny_name(seed)
    params = {
        "date_str": date.isoformat(),
        "codename": codename,
        "audio_device": random.choice(AUDIO_DEVICES),
        "resolution": random.choice(RESOLUTIONS),
        "reminder_title": random.choice(REMINDER_TITLES),
        "reminder_note": random.choice(REMINDER_NOTES),
        "offset_hours": random.choice([0.5, 1, 2, 3]),
        "note_headline": random.choice(NOTE_HEADLINES),
        "note_body": random.choice(NOTE_BODIES),
        "draft_prompt": random.choice(DRAFT_PROMPTS),
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
