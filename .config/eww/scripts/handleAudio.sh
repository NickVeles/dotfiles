#!/bin/bash

# handleAudio.sh - handles volume and updates the corresponding stream icon in eww

sleep 1

# Update the microphone volume and icon
updateMic() {

    local microphone
    microphone="alsa_input.pci-0000_07_00.4.analog-stereo"
    local volume
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
}

# Update the output volume and icon
updateOut() {

    local volume
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
}

# Run the scripts at least once
updateMic
updateOut

# Subscribe to PulseAudio events
pactl subscribe | while read -r event; do
    if echo "$event" | grep -q "change"; then

        # When a change event occurs:
        updateMic
        updateOut
    fi
done
