class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        n=days[-1]+1
        dp=[0]*n
        d=0

        for i in range(n):
            if i!=days[d]:
                dp[i]=dp[i-1]
            else:
                d+=1
                dp[i]=min(
                    dp[max(0,i-1)]+costs[0],
                    dp[max(0,i-7)]+costs[1],
                    dp[max(0,i-30)]+costs[2]
                )
        return dp[-1]

           

