import time

class memAllocatorFixed:
    def __init__(self,mb_to_allocate,time_in_s):
        self.mb_to_allocate = mb_to_allocate
        self.time_in_s = time_in_s
    
    def allocate(self):
        print("allocating {} MBs for {} seconds".format(self.mb_to_allocate,self.time_in_s))
        test = bytearray(round(self.mb_to_allocate)*1000000) 
        time.sleep(self.time_in_s)


if __name__ == "__main__":
    import sys
    if(len(sys.argv) != 3):
        sys.exit(1)
    memAllocatorFixed(int(sys.argv[1]),int(sys.argv[2])).allocate()