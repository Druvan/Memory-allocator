#!/bin/bash
test=$(cat /proc/meminfo | grep MemTotal | sed -e 's/ /\n/g' | tail -2 | head -1)
echo "total_ram" . $test
cpu_percent=$1
make run tot_ram=$test mem_percent=$2 time=$3 &
stress-ng --cpu 1 --cpu-load $cpu_percent -t $3