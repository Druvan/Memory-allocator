import time
#!/usr/bin/python3

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if(len(sys.argv) != 4):
    print("Wrong number of arguments, Should be total_ram, mem_percent, time_in_s")
    sys.exit(1)
    
total_ram = int(sys.argv[1])*1000
mem_percent = int(sys.argv[2])
time_in_s = int(sys.argv[3])

if (total_ram > 0 and mem_percent >= 0 and time_in_s > 0):
    
    bytes_to_allocate = total_ram*mem_percent*0.01
    print (bytes_to_allocate)
    test = bytearray(round(bytes_to_allocate)) 
    time.sleep(time_in_s)
else:
    print("Args needs to be , total_ram: > 0 is ", total_ram,", mem_percent: >= 0 is ", mem_percent, ", time_in_s: > 0 is ",time_in_s," \n")
    sys.exit(1) 
    
