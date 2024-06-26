#!/bin/bash

{ echo "🗑 Wipe Clipboard History"; cliphist list; } | rofi -dmenu -p "Clipboard" | xargs -r -I '{}' sh -c '[ "{}" = "🗑 Wipe Clipboard History" ] && cliphist wipe || cliphist decode "{}" | wl-copy'
