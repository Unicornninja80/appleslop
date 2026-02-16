-- Title: Finder Desktop Sweep
-- Generated on 2026-02-16
-- Codename: Sneaky Crunch Byte
set archiveFolder to (path to documents folder as text) & "Sorted Desktop"
tell application "Finder"
    if not (exists folder archiveFolder) then
        make new folder at (path to documents folder) with properties {name:"Sorted Desktop"}
    end if
    set desktopItems to every item of desktop
    repeat with anItem in desktopItems
        move anItem to folder archiveFolder
    end repeat
end tell
display notification "Desktop cleared to Sorted Desktop" with title "Sneaky Crunch Byte"
