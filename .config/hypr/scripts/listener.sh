#!/bin/sh

# listener.sh - handles Hyprland event changes.

fetch_all_workspaces() {
  # fetch the IDs of all workspaces:
  # - that are not secret (id < 0)
  # - in the JSON format, e.g. [1, 2, 3]
  hyprctl workspaces -j | jq -c '[.[] | select(.id > 0) | .id] | sort'
}

fetch_active_workspace() {
  # fetch the ID of the active workspace
  hyprctl activeworkspace -j | jq '.id'
}

handle() {
  case $1 in
    workspace*)
      # Status Bar - all workspaces
      eww update workspaces="$(fetch_all_workspaces)" &&
      # Status Bar - active workspace
      eww update acSpace="$(fetch_active_workspace)";;
  esac
}

socat -U - UNIX-CONNECT:$XDG_RUNTIME_DIR/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock | while read -r line; do handle "$line"; done