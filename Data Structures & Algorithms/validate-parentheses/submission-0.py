class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack for opening brackets
        # Iterate through characters in the str
            # Add opening brackets to opening stack
            # When finding a closing bracket, check if its corresponding open
            # bracket is at the top of the opening stack (pop it)
                # If it corresponds, continue
                # If it doesn't or there is nothing in stack, return false 
                # (brackets are not closed in proper order/type)
        # If there are still items in opening stack, there are unclosed parentheses
        # (return false)

        opening = []

        for i in range(len(s)):
            if s[i] == ')':
                if not opening or opening.pop() != '(':
                    return False
            elif s[i] == '}':
                if not opening or opening.pop() != '{':
                    return False
            elif s[i] == ']':
                if not opening or opening.pop() != '[':
                    return False
            else:
                opening.append(s[i])
        
        if opening:
            return False
        return True
        

        