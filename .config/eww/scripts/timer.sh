#!/bin/bash

initialSeconds=$(eww get initialTS)
action=$(eww get timerAction)
seconds=$(eww get timerSeconds)
running=$(eww get timerRunning)
remaining=$(date -u -d @"$seconds" +'%-Hh %-Mm %-Ss')

# Reset the timer
if [ $action == "reset" ]; then

    eww update timerSeconds=$initialSeconds
    eww update timerRunning=false
    eww update timerIcon=timer_off
    eww update timerAction=none

    eww update timerTooltip=" Start a timer "

# Turn running OFF
elif [ $action == "toggle" ] && [ "$running" == "true" ]; then

    eww update timerSeconds=$seconds
    eww update timerRunning=false
    eww update timerIcon=timer_off
    eww update timerAction=none

    eww update timerTooltip=" Paused "

# Turn running ON
elif [ $action == "toggle" ] && [ "$running" == "false" ]; then

    eww update timerRunning=true
    eww update timerIcon=timer
    eww update timerAction=none

    eww update timerTooltip=" Break in ~ $remaining "

# Decrement the seconds
elif [ $seconds -gt 0 ] && [ "$running" == "true" ]; then

    seconds=$(($seconds - 5))
    eww update timerSeconds=$seconds

    eww update timerTooltip=" Break in ~ $remaining "

# Finish the timer
elif [ $seconds == 0 ] && [ "$running" == "true" ]; then

    eww update timerSeconds=$initialSeconds
    eww update timerRunning=false
    eww update timerIcon=timer_off
    eww update timerAction=none

    eww update timerTooltip=" Start a timer "

    # Play the sound
    paplay $HOME/.sounds/notif3.mp3 --volume 46000 &

    # Show the notification
    notification=$(notify-send -t 0 -i $HOME/.config/eww/icons/timer.svg "Break Time! 😎" " lock your screen <span color='#FFD866'></span>...\n make some tea <span color='#FFD866'>󰶞</span>,\n exercise <span color='#FFD866'>󱅝</span>...?" --action="ok=OK")

    case $notification in
        "ok")
            playerctl pause
            hyprlock
            ;;
        *)
            ;;
    esac

fi