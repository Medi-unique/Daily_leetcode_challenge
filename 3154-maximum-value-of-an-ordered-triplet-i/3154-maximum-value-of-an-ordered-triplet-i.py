class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = float('-inf')
        for j in range(len(nums)):
            for e in range(1 + j, len(nums)):
                for s in range(1 + e , len(nums)):
                    process = (nums[j] - nums[e]) * nums[s]
                    result = max(process, result)
        return max(result, 0 )
        