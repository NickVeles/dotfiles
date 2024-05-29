#!/bin/sh

layout=$(eww get keyboard)

if [ "$layout" = "US" ]; then
    hyprctl keyword input:kb_layout pl
    eww update keyboard=PL
else
    hyprctl keyword input:kb_layout us
    eww update keyboard=US
fi

paplay $HOME/.sounds/switch.mp3 --volume 36000