#!/bin/bash

layout=$(hyprctl devices -j |
    jq -r '.keyboards[] | .active_keymap' |
    head -n1 |
    cut -c1-2 |
    tr 'a-z' 'A-Z')

if [ "$layout" -eq "PO" ]; then
    hyprctl keyword input:kb_layout pl
    notify-send "PL" "Changed to Polish Keyboard Layout"
else
    hyprctl keyword input:kb_layout pl
    notify-send "US" "Changed to US Keyboard Layout"
fi

paplay $HOME/.sounds/switch.mp3 --volume 36000