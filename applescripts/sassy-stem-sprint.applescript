-- Title: Notes Brain Dump
            -- Generated on 2026-02-14
            -- Codename: Sassy Stem Sprint
            set noteHeadline to "Meeting crumbs"
            set noteBody to "List what should be delegated this week."
            tell application "Notes"
                activate
                set targetFolder to first folder whose name is "Notes"
                make new note at targetFolder with properties {name:noteHeadline, body:noteHeadline & "

" & noteBody}
            end tell
