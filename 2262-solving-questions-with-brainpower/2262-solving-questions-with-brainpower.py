class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*n
        dp[-1]=questions[-1][0]

        for i in range(n-2,-1,-1):
            p,ind=questions[i]

            if i+ind+1 <n:
                dp[i]=max(dp[i+1],p+dp[i+ind+1])
            else:
                dp[i]=max(p,dp[i+1])
        
        return max(dp)
        