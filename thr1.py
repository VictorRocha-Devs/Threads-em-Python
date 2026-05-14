import threading
import time

def tarefa(id):
    time.sleep(0.5)
    print(f"Thread #{id}")

threads = []
for i in range(5):
    t = threading.Thread(target=tarefa, args=(i,))
    threads.append(t)
    t.start()