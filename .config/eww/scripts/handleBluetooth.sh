#!/bin/sh

# Function to check Bluetooth connectivity and print connection status
updateBluetooth() {

    local device_name
    device_name=$(bluetoothctl info | grep "Name" | cut -d ' ' -f 2-)
    
    if [ -n "$device_name" ]; then
        eww update bluetoothName="$device_name"
        eww update bluetoothIcon="bluetooth"
        eww update bluetoothEnabled=true
    else
        eww update bluetoothName="Not connected"
        eww update bluetoothIcon="bluetooth_off"
        eww update bluetoothEnabled=false
    fi
}

# Run the function at least once
updateBluetooth

# Monitor Bluetooth connection changes
bluetoothctl | while read -r line; do
    if [[ "$line" == *"Connected:"* ]]; then
        updateBluetooth
    fi
done
