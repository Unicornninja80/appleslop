-- Title: Audio Route Snap
-- Generated on 2026-02-21
-- Codename: Saucy Crunch Byte
set targetDevice to "AirPods Pro"
do shell script "SwitchAudioSource -s '" & targetDevice & "'" -- requires https://github.com/deweller/switchaudio-osx
display notification "Sound routed to " & targetDevice with title "Saucy Crunch Byte"
