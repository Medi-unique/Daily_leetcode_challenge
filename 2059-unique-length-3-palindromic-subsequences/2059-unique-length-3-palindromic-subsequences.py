class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        visited=set()
        ans=0
        for i,l in enumerate(s):
            if l not in visited:
                visited.add(l)
                r=s.rindex(l)
                ans+=len(set(s[i+1:r]))
        return ans

        