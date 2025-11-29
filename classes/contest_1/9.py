from typing import Any

class Queue:
    def __init__(self):
        self.tail = -1
        self.arr = []
        
    def push(self, item) -> None:
        self.arr.insert(0, item)
        self.tail += 1
        
    def pop(self) -> Any:
        item = self.arr[self.tail]
        del self.arr[self.tail]
        self.tail -= 1
        return item
    
    def is_empty(self) -> bool:
        return self.tail == -1
    
    
queue = Queue()
for item in ("Hello,", "world!"):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop())

