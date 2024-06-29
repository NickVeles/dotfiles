#!/bin/bash

# List all input sources
input_sources=$(pamixer --list-sources | grep input | awk '{print $2}' | sed 's/"//g')

# Variable to store the final mute status
final_status=""

# Iterate over each input source
for source in $input_sources; do
    # Toggle the mute status for each input source
    pamixer --toggle-mute --source "$source"

    # Get the mute status after toggling
    mute_status=$(pamixer --get-mute --source "$source")

    # Store the final status for sound notification
    final_status=$mute_status
done

# Play the corresponding sound based on the final status
if [ "$final_status" = "true" ]; then
    paplay ~/.sounds/mute.mp3 --volume 36000
else
    paplay ~/.sounds/unmute.mp3 --volume 36000
fi
