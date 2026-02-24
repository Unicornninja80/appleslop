-- Title: Audio Route Snap
-- Generated on 2026-02-24
-- Codename: Retro Fruit Loop
set targetDevice to "External Monitor"
do shell script "SwitchAudioSource -s '" & targetDevice & "'" -- requires https://github.com/deweller/switchaudio-osx
display notification "Sound routed to " & targetDevice with title "Retro Fruit Loop"
