#!/bin/bash
test=$(cat /proc/meminfo | grep MemTotal | sed -e 's/ /\n/g' | tail -2 | head -1)
echo $test
make run tot_ram=$test mem_procent=50 time=10