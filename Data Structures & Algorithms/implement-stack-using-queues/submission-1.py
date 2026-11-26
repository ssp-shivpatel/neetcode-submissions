from collections import deque

# Space: O(n)
class MyStack:
    # Queues -- add to one end, access/remove from the other
    # Stacks -- add to one end, access/remove from same end

    def __init__(self):
        self.data = deque()
        self.size = 0
        
    # Our goal with pushing to a stack is to represent the new element at front
    # of the queue
    # Therefore, when we enqueue new to the back, simply dequeue the elements at the 
    # front and enqueue them at the back until the new element's at the front
    # Runtime: O(n)
    def push(self, x: int) -> None:
        self.data.appendleft(x)
        for i in range(self.size):
            self.data.appendleft(self.data.pop())

        self.size += 1

    # Runtime: O(1)
    def pop(self) -> int:
        self.size -= 1
        return self.data.pop()

    # Runtime: O(1)
    def top(self) -> int:
        return self.data[-1]

    # Runtime: O(1)
    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()