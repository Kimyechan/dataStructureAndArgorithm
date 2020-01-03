#LifoQueue()로 큐 만들기 (LIFO(Last-In, First-Out)

import queue

data_queue = queue.LifoQueue()

data_queue.put("funcoding")
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())
