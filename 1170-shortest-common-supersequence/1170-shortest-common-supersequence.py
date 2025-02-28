class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n=len(str1) 
        m=len(str2)
        dp=[[0]*(m+1) for i in range(1+n)]
        for row in range(n+1):
            dp[row][0]=row
        for col in range(m+1):
            dp[0][col]=col

        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
        l=dp[n][m]
        p1=n;p2=m
        ans=""
        while(p1>0 and p2>0):
            if str1[p1-1]==str2[p2-1]:
                ans+=str1[p1-1]
                p1-=1
                p2-=1
            elif dp[p1-1][p2]<dp[p1][p2-1]:
                ans+=str1[p1-1]
                p1-=1
            else:
                ans+=str2[p2-1]
                p2-=1
        while p1>0:
            ans+=str1[p1-1]
            p1-=1
        while p2>0:
            ans+=str2[p2-1]
            p2-=1
        return ans[::-1]
        