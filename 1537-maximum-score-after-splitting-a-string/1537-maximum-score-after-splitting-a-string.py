class Solution:
    def maxScore(self, s: str) -> int:
        count=Counter(s)
        l=count['1']
        r=0
        size=len(s)
        ans=0
        for i in range(1,size):
            if s[i-1]=='0':
                r+=1
            else:
                l-=1
            ans=max(ans,r+l)
        return ans