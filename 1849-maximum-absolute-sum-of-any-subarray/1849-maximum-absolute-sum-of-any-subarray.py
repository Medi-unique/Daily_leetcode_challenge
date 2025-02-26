class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxVal, minVal = 0, 0
        prev = 0
        for i in range(0, len(nums)):
            nums[i] += prev
            maxVal = max(maxVal, nums[i])
            minVal = min(minVal, nums[i])
            prev = nums[i]
        return maxVal - minVal