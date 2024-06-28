#!/bin/bash

microphone="alsa_input.pci-0000_07_00.4.analog-stereo.4"
# Toggle the source
pamixer --toggle-mute --source "$microphone"

# Check if the source is muted
if [ $(pamixer --get-mute --source "$microphone") = "true" ]; then
    # Play mute sound
    paplay $HOME/.sounds/mute.mp3 --volume 36000
else
    # Play unmute sound
    paplay $HOME/.sounds/unmute.mp3 --volume 36000
fi
