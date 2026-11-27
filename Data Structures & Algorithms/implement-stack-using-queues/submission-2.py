from collections import deque

class MyStack:

    def __init__(self):
        self.data = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.data.appendleft(x)
        for i in range(self.size):
            self.data.appendleft(self.data.pop())
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