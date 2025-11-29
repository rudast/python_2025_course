from typing import Any


class StackNode:
    def __init__(self, value: Any, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, item: Any) -> None:
        temp = None
        if self.top:
            temp = self.top

        self.top = StackNode(item, temp)
        
    def pop(self) -> Any:
        if self.top:
            current = self.top.value
            self.top = self.top.next
                
            return current
        return None
    
    def is_empty(self) -> bool:
        return self.top
    
stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")
