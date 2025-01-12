class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack = []

        if len(s)%2!=0:
            return False

        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        
        stack = []
        for i in range(len(s)-1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return True