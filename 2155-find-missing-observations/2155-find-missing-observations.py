class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        totalsum=mean*(n+m)
        missingsum=totalsum-sum(rolls)
        if missingsum>6*n or missingsum<n:
            return []
        res=[]
        while n:
            curr=min(6,missingsum-n+1)
            res.append(curr)
            missingsum-=curr
            n-=1
        return res
        