class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        s=list(s)
        p=list(part)
        n,m=len(s),len(part)
        stack=[]
        for i in range(n):
            stack.append(s[i])
            if p == stack[len(stack)-m:]:
                for i in range(m):
                    stack.pop()
            
        return "".join(stack)
        