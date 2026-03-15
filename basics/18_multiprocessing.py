# Sample: Python Multiprocessing Example
from multiprocessing import Process
import os
import time

def worker(name):
    for i in range(3):
        print(f"Process {name} (PID {os.getpid()}): {i}")
        time.sleep(1)

processes = []
for n in ['A', 'B']:
    p = Process(target=worker, args=(n,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("All processes finished.")
