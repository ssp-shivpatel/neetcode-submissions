class MyQueue:

    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, x: int) -> None:
        aux = []
        while len(self.data) > 0:
            aux.append(self.data.pop())
        
        self.data.append(x)
        while len(aux) > 0:
            self.data.append(aux.pop())
        
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.data.pop()
        
    
    def peek(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return len(self.data) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()