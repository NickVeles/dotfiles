#!/bin/sh

volume=$(pamixer --get-volume-human)

if [ "$volume" = "muted" ]; then
    # Set the icon to muted if it's muted
    eww update outIcon="volume_mute"

elif [ "$volume" = "0%" ]; then
    # Set the icon to off if the volume is 0%
    eww update outIcon="volume_off"

else
    # Set the icon to default
    eww update outIcon="volume"
fi

# Set the volume level
eww update outVolume="$volume"