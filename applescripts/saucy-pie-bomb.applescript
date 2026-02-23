-- Title: Audio Route Snap
-- Generated on 2026-02-23
-- Codename: Saucy Pie Bomb
set targetDevice to "MacBook Pro Speakers"
do shell script "SwitchAudioSource -s '" & targetDevice & "'" -- requires https://github.com/deweller/switchaudio-osx
display notification "Sound routed to " & targetDevice with title "Saucy Pie Bomb"
