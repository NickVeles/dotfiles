#!/bin/bash

# Play the sound
paplay $HOME/.sounds/notif3.mp3 --volume 46000 &

# Show the notification
notification=$(notify-send -t 0 -i "emoji-recent-symbolic" "Break Time! 😎" " lock your screen <span color='#FFD866'></span>...\n make some tea <span color='#FFD866'>󰶞</span>,\n exercise <span color='#FFD866'>󱅝</span>...?" --action="ok=Ok")

case $notification in
    "ok")
        playerctl pause
        hyprlock
        ;;
    *)
        ;;
esac