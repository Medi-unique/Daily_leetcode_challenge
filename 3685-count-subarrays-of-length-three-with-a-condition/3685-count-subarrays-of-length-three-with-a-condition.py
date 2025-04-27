class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        l, r = 0, 2
        while r < len(nums):
            if (nums[l] + nums[r]) * 2 == nums[l + 1]:
                count += 1
            l += 1
            r += 1
        return count