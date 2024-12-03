class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans,i,k=[],0,0
        while k<len(spaces):
            if i==spaces[k]:
                ans.append(' ')
                k+=1
            ans.append(s[i])
            i+=1
        while i<len(s):
            ans.append(s[i])
            i+=1
        return ''.join(ans)