#!/bin/bash

# Define the directory path
target=$1
mode=$2
directory="$HOME/Pictures/Screenshots/$(date +'%Y_%m')"
file="$directory/$(date +'%d_%H%M%S').png"

# Check edit mode
handle_mode() {
    if [ "$mode" == "edit" ]; then
        swappy -f $(grimblast copysave "$target" "$file")
    else
        grimblast copysave "$target" "$file"
    fi 
}

# Check if the directory exists
if [ -d "$directory" ]; then
    # Directory exists, prtsc to the directory
    handle_mode
else
    # Directory doesn't exist, create the directory and prtsc to it
    mkdir -p "$directory"
    handle_mode
fi
