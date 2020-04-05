from collections import deque
queue = deque(["Ram","Tarun","Asif","John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Sathish")
print(queue)
print(queue.popleft())
print(queue)
