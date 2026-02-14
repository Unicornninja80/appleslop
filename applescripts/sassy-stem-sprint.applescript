-- Title: Note Capsule
            -- Generated on 2026-02-14
            set noteHeadline to "Debug diary"
            set noteBody to "List one lesson learned from today."
            tell application "Notes"
                activate
                set targetFolder to first folder whose name is "Notes"
                make new note at targetFolder with properties {name:noteHeadline, body:noteHeadline & "

" & noteBody}
            end tell
