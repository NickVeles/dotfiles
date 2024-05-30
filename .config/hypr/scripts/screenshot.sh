#!/bin/bash

# Define the directory path
target=$1
directory="$HOME/Pictures/Screenshots/$(date +'%Y_%m')"
file="$directory/$(date +'%d_%H%M%S').png"

# Check if the directory exists
if [ -d "$directory" ]; then
    # Directory exists, prtsc to the directory
    grimblast copysave "$target" "$file"
else
    # Directory doesn't exist, create the directory and prtsc to it
    mkdir -p "$directory"
    grimblast copysave "$target" "$file"
fi