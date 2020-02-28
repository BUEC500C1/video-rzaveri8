import queue

def init():
    global id
    global q
    global processes
    global max_threads

    id = 0  # identifier for ids
    q = queue.Queue(maxsize=50)
    processes = {}  
    max_threads = 4