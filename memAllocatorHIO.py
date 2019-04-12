from harmonicPE.daemon import listen_for_tasks
from memAllocator import memAllocator
import sys

def process_data(message_bytes):
    ma = memAllocator(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
    print()
    ma.run()


# Start the daemon to listen for tasks:
listen_for_tasks(process_data)