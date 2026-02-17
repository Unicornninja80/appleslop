-- Title: Dark Mode Flip
-- Generated on 2026-02-17
-- Codename: Galactic Crunch Byte
tell application "System Events"
    tell appearance preferences
        set dark mode to not dark mode
    end tell
end tell
display notification "Dark mode toggled." with title "Galactic Crunch Byte"
