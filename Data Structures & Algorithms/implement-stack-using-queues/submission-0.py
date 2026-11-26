from collections import deque

class MyStack:
    # Queues -- add to one end, access/remove from the other
    # Stacks -- add to one end, access/remove from same end


    def __init__(self):
        self.data = deque()
        self.size = 0
        
    # Whenever you add to the queue, you pop all existing elements into a
    # separate queue, add the new element into the main queue, and place 
    # existing elements back in reverse order
    def push(self, x: int) -> None:
        aux = deque()
        while self.data:
            aux.appendleft(self.data.pop())

        self.data.appendleft(x)
        while aux:
            self.data.appendleft(aux.pop())
        
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()