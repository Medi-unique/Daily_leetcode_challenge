class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        dp = [False] * ((sum(nums) // 2) + 1)
        dp[0] = True
        for num in nums:
            for i in range((sum(nums) // 2), num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[(sum(nums) // 2)]