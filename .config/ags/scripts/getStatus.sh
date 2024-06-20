#!/bin/bash

# Get CPU usage
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}' | xargs printf "%.0f")

# Get CPU temperature
cpu_temp=$(sensors | grep 'Tctl:' | awk '{print $2}' | sed 's/[^0-9.]//g')
cpu_temp=$(printf "%.0f" "$cpu_temp")

# Get RAM usage
ram_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}' | xargs printf "%.0f")

# Get Disk usage
disk_usage=$(df / | grep / | awk '{print $5}' | sed 's/[^0-9]//g')

# Get GPU usage and temperature (NVIDIA GPUs)
if command -v nvidia-smi &> /dev/null
then
    gpu_usage=$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits)
    gpu_temp=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits)
    # gpu_usage="${gpu_usage}"
    gpu_temp=$(printf "%.0f" "$gpu_temp")
else
    gpu_usage="N/A"
    gpu_temp="N/A"
fi

# Output
# CPU %   RAM %   GPU %
# CPUC   DSK %   GPUC
echo "{ \"cpu_usage\": { \"color\": \"#65D6C4\", \"value\": $cpu_usage }, \"ram_usage\": { \"color\": \"#A9DC76\", \"value\": $ram_usage }, \"gpu_usage\": { \"color\": \"#FC9867\", \"value\": $gpu_usage }, \"cpu_temp\": { \"color\": \"#AB9DF2\", \"value\": $cpu_temp }, \"disk_usage\": { \"color\": \"#FFD866\", \"value\": $disk_usage }, \"gpu_temp\": { \"color\": \"#FF6188\", \"value\": $gpu_temp } }"

