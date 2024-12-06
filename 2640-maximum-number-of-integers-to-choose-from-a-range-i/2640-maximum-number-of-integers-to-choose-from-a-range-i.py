class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count=0
        curr=0
        check=set(banned)
        for i in range(1,n+1):
            if i not in check:
                if curr+i <= maxSum:
                    curr+=i
                    count+=1
        return count

        