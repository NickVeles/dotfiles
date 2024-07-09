#!/bin/bash

paplay $HOME/.sounds/switch.mp3 --volume 36000 &

layout=$(hyprctl devices -j |
    jq -r '.keyboards[] | .active_keymap' |
    head -n1 |
    cut -c1-2 |
    tr 'a-z' 'A-Z')

if [ "$layout" == "PO" ]; then
    hyprctl keyword input:kb_layout us
    notify-send "<span color='#458588'>English</span>" "Changed to US Keyboard Layout"
else
    hyprctl keyword input:kb_layout pl
    notify-send "<span color='#FB4934'>Polish</span>" "Changed to Polish Keyboard Layout"
fi
