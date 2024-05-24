#!/bin/sh

# handleAudio.sh - handles volume and updates the corresponding stream icon in eww

sleep 1

# Run the scripts at least once
$HOME/.config/eww/scripts/updateMic.sh
$HOME/.config/eww/scripts/updateOut.sh

# Subscribe to PulseAudio events
pactl subscribe | while read -r event; do
    if echo "$event" | grep -q "change"; then

        # When a change event occurs:
        $HOME/.config/eww/scripts/updateMic.sh
        $HOME/.config/eww/scripts/updateOut.sh
    fi
done
