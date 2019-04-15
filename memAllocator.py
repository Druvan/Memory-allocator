import time
#!/usr/bin/python3
import subprocess
import sys
import re

class memAllocator:
    def __init__(self, cpu_percent, mem_percent, time_in_s):
        self.cpu_percent = cpu_percent
        self.mem_percent = mem_percent
        self.time_in_s = time_in_s


    def run(self):
        print("inputs: ",self.cpu_percent, self.mem_percent,self.time_in_s)
        with open('/proc/meminfo') as f:
            meminfo = f.read()
        matched = re.search(r'^MemTotal:\s+(\d+)', meminfo)
        if matched: 
            total_ram = int(matched.groups()[0])*1000
        print("total ram: ",total_ram)
        if (total_ram > 0 and self.mem_percent >= 0 and self.time_in_s > 0 and self.cpu_percent >= 0):
            bytes_to_allocate = total_ram*self.mem_percent*0.01
            print("bytes_to_allocate: ",bytes_to_allocate)
            test = bytearray(round(bytes_to_allocate)) 
            if(self.cpu_percent > 0):
                cpu_ret = subprocess.Popen(["stress-ng", "--cpu" ,"1", "--cpu-load", str(self.cpu_percent) ,"-t" ,str(self.time_in_s)])
            time.sleep(self.time_in_s)
        else:
            print("Args needs to be , total_ram: > 0 is ", total_ram,", cpu_percent: >= 0 is ", self.cpu_percent, " mem_percent: >= 0 is ", self.mem_percent, ", time_in_s: > 0 is ",self.time_in_s," \n")
            sys.exit(1) 

        if(self.cpu_percent > 0):
            cpu_ret.wait()
            if(cpu_ret.returncode != 0):
                print("something went wrong in cpu stress",cpu_ret.returncode,cpu_ret.stdout)


if __name__ == "__main__":
    if(len(sys.argv) != 4):
        print("Wrong number of arguments, Should be cpu_percent, mem_percent, time_in_s")
        sys.exit(1)
    memAllocator(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])).run()