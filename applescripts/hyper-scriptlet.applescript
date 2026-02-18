-- Title: Reminders Momentum
-- Generated on 2026-02-18
-- Codename: Hyper Scriptlet
set reminderTitle to "Hydration break"
set reminderNotes to "Brainstorm tomorrow's top 3 priorities."
set dueDate to (current date) + (3 * hours)
tell application "Reminders"
    activate
    make new reminder with properties {name:reminderTitle, body:reminderNotes, remind me date:dueDate}
end tell
