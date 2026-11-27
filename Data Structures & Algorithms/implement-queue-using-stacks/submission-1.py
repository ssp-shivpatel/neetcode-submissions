class MyQueue:

    def __init__(self):
        self.stack = []
        self.r_stack = []
        self.size = 0

    # Runtime: O(1)
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

    # Runtime: O(1) amortized
    # The stack in reverse order holds the element we want to pop at top (O(1))
    # Build the reverse stack if it's empty by popping off of the push stack (O(n))
        # Return the last element popped off push stack in this case
    def pop(self) -> int:
        if len(self.r_stack) > 0:
            self.size -= 1
            return self.r_stack.pop()

        while len(self.stack) > 1:
            self.r_stack.append(self.stack.pop())

        self.size -= 1
        return self.stack.pop()
    
    # Runtime: O(1) amortized
    # Same as pop -- but just return value, instead of popping
        # We can move last value to r_stack since we're not removing it
    def peek(self) -> int:
        if len(self.r_stack) > 0:
            return self.r_stack[-1]
        
        while len(self.stack) >  0:
            self.r_stack.append(self.stack.pop())
        
        return self.r_stack[-1]

        
        
    # Runtime: O(1)
    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()