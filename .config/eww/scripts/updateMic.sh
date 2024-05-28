#!/bin/sh

microphone="alsa_input.pci-0000_07_00.4.analog-stereo"
volume=$(pamixer --get-volume-human --source "$microphone")

if [ "$volume" = "muted" ]; then
    # Set the icon to muted if it's muted
    eww update micIcon="mic_mute"

else
    # Set the icon to default
    eww update micIcon="mic"
fi

# Set the volume level
eww update micVolume="$volume"