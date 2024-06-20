#!/bin/bash

layout=$(hyprctl devices -j |
    jq -r '.keyboards[] | .active_keymap' |
    head -n1 |
    cut -c1-2 |
    tr 'a-z' 'A-Z')

if [ "$layout" == "PO" ]; then
    hyprctl keyword input:kb_layout us
    notify-send $layout "Changed to US Keyboard Layout"
else
    hyprctl keyword input:kb_layout pl
    notify-send $layout "Changed to Polish Keyboard Layout"
fi

paplay $HOME/.sounds/switch.mp3 --volume 36000