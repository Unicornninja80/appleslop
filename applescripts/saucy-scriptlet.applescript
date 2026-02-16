-- Title: Audio Route Snap
-- Generated on 2026-02-15
-- Codename: Saucy Scriptlet
set targetDevice to "External Monitor"
do shell script "SwitchAudioSource -s '" & targetDevice & "'" -- requires https://github.com/deweller/switchaudio-osx
display notification "Sound routed to " & targetDevice with title "Saucy Scriptlet"
