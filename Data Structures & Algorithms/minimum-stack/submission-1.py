class MinStack:
    def __init__(self):
        self.data = []
        self.minimum = None
        
    def push(self, val: int) -> None:
        self.data.append(val)
        if self.minimum == None or val < self.minimum:
            self.minimum = val

    # Runtime: O(1) amortized
    # Only when removing min element do we scan the stack for another min elem
        # Since it's a stack, we must move elements to an aux stack when scanning
        # and move back after we checked all elements for a new min

        # If we find an elem equal to the previous min elem, that must be our
        # new min elem and we can stop scanning early.
    def pop(self) -> None:
        popped = self.data.pop()
        if popped == self.minimum:
            self.minimum = None
            temp_stack = []

            while len(self.data) > 0:
                potential_min = self.data.pop()
                temp_stack.append(potential_min)

                if potential_min == popped:
                    self.minimum = popped
                    break
                if not self.minimum or potential_min < self.minimum:
                    self.minimum = potential_min
            
            while len(temp_stack) > 0:
                self.data.append(temp_stack.pop())
            
    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def getMin(self) -> int:
        return self.minimum
