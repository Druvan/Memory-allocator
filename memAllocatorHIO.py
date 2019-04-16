from harmonicPE.daemon import listen_for_tasks
from memAllocator import memAllocator
from os import environ

def process_data(message_bytes):
    print("Running memAllocator")
    cpulevel = int(environ.get("CPU_LEVEL", 5))
    memlevel = int(environ.get("MEM_LEVEL", 20))
    time = int(environ.get("TIME", 15))
    ma = memAllocator(cpulevel,memlevel,time)
    ma.run()


# Start the daemon to listen for tasks:
listen_for_tasks(process_data)