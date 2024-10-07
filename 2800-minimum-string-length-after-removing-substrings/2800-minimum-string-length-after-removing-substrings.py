class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for i in s:
            stack.append(i)
            if len(stack) >= 2 and stack[-1] == "B" and stack[-2] == "A":
                stack.pop()
                stack.pop()
            elif len(stack) >= 2 and stack[-1] == "D" and stack[-2] == "C":
                stack.pop()
                stack.pop()

        return len(stack)
            
