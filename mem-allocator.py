import time
#!/usr/bin/python3
import subprocess
import sys
import re

if(len(sys.argv) != 4):
    print("Wrong number of arguments, Should be cpu_percent, mem_percent, time_in_s")
    sys.exit(1)

with open('/proc/meminfo') as f:
    meminfo = f.read()
matched = re.search(r'^MemTotal:\s+(\d+)', meminfo)
if matched: 
    total_ram = int(matched.groups()[0])*1000



print("total: ",total_ram)
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

    
cpu_percent = int(sys.argv[1])
mem_percent = int(sys.argv[2])
time_in_s = int(sys.argv[3])

if (total_ram > 0 and mem_percent >= 0 and time_in_s > 0 and cpu_percent >= 0):
    
    bytes_to_allocate = total_ram*mem_percent*0.01
    print (bytes_to_allocate)
    test = bytearray(round(bytes_to_allocate)) 
    if(cpu_percent > 0):
        cpu_ret = subprocess.Popen(["stress-ng", "--cpu" ,"1", "--cpu-load", str(cpu_percent) ,"-t" ,str(time_in_s)])
    time.sleep(time_in_s)
else:
    print("Args needs to be , total_ram: > 0 is ", total_ram,", mem_percent: >= 0 is ", mem_percent, ", time_in_s: > 0 is ",time_in_s," \n")
    sys.exit(1) 

if(cpu_percent > 0):
    cpu_ret.wait()
    if(cpu_ret.returncode != 0):
        print("something went wrong in cpu stress",cpu_ret.returncode,cpu_ret.stdout)
    
