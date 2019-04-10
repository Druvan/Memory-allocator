#!/bin/bash
total_ram=$(cat /proc/meminfo | grep MemTotal | sed -e 's/ /\n/g' | tail -2 | head -1)
cpu_percent=$1
python3 mem-allocator.py $total_ram $2 $3 &
stress-ng --cpu 1 --cpu-load $cpu_percent -t $3
