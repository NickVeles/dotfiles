#!/bin/bash

# Function to check internet connectivity
updateConnection() {

    local connection
    name=$(nmcli -t -f NAME connection show --active | head -n 1)
    device=$(nmcli -t -f DEVICE connection show --active | head -n 1)

    if nmcli networking connectivity check | grep -q "full"; then
        eww update networkIcon="wifi"
        eww update networkName="$name"
        eww update networkDevice="$device"
    else
        eww update networkIcon="wifi_off"
        eww update networkName="Disconnected"
        eww update networkDevice="None"
    fi
}

# Run the function at least once
updateConnection

# Monitor network changes using nmcli
nmcli monitor | while read -r line; do
    updateConnection
done
