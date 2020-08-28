#PriorityQueue() 만들기
import queue

data_queue = queue.PriorityQueue()

data_queue.put((15, "USA"))
data_queue.put((10, "korea"))
data_queue.put((20, "china"))

print(data_queue.get())
