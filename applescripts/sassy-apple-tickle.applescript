-- Title: Notes Brain Dump
            -- Generated on 2026-02-19
            -- Codename: Sassy Apple Tickle
            set noteHeadline to "Idea fragments"
            set noteBody to "Capture three bullet points about what's buzzing."
            tell application "Notes"
                activate
                set targetFolder to first folder whose name is "Notes"
                make new note at targetFolder with properties {name:noteHeadline, body:noteHeadline & "

" & noteBody}
            end tell
