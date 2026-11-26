class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Stack
        # Runtime: O(n)
        # Space: O(n)


        # Create a list-base stack that stores what records we've seen before
        # Iterate through the array, keeping track of a res (sum) vr
            # Add each numerical value to a res (sum) var

            # For + operations, just add the top/last two values in the list
            # based stack into res. Make sure to add this sum to the stack.

            # For D operations, simply double the the last value in the stack and
            # add to res. Then, add this doubled value to the stack.

            # Whenever we remove a record, we can pop that record off the stack
            # and easily remove its value from the sum even if we have a row of C's
        
        stack = []
        res = 0

        for i in range(len(operations)):
            if operations[i] == "+":
                score = stack[len(stack) - 1] + stack[len(stack) - 2]
                res += score
                stack.append(score)
            elif operations[i] == "D":
                score = stack[len(stack) - 1] * 2
                res += score
                stack.append(score)
            elif operations[i] == "C":
                res -= stack[len(stack) - 1]
                stack.pop()
            else:
                score = int(operations[i])
                res += score
                stack.append(score)
        
        return res

