from harmonicPE.daemon import listen_for_tasks
from memAllocator import memAllocator

def process_data(message_bytes):
    ma = memAllocator(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
    ma.run()


# Start the daemon to listen for tasks:
listen_for_tasks(process_data)