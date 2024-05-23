#!/bin/sh

# handleAudio.sh - handles volume and updates the corresponding stream icon in eww

# Run the scripts at least once
exec $HOME/.config/eww/scripts/updateOut.sh
exec $HOME/.config/eww/scripts/updateMic.sh

# Subscribe to PulseAudio events
pactl subscribe | while read -r event; do
    if echo "$event" | grep -q "change"; then

        # When a change event occurs:
        ./updateOut.sh
        ./updateMic.sh
    fi
done
