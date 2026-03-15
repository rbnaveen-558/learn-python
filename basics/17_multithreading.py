# Sample: Python Multithreading Example
import threading
import time

def worker(name):
    for i in range(3):
        print(f"Thread {name}: {i}")
        time.sleep(1)

threads = []
for n in ['A', 'B']:
    t = threading.Thread(target=worker, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished.")
