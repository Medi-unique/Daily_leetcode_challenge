class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo=defaultdict(int)
        n=len(nums)
        def check(i,s):
            if i >= n:
                if s==target:
                    return 1
                
                return 0

            if (i,s) not in memo:
                pos=check(i+1,s+nums[i])
                neg=check(i+1,s-nums[i])
                cur=pos+neg
                memo[(i,s)]=cur
            return memo[(i,s)]
            
        return check(0,0)


