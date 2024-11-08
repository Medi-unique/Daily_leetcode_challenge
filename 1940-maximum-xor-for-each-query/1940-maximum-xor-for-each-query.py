class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        val= (1<<maximumBit) - 1
        temp = 0
        for i in nums:
            temp ^= i
        res = []
        for i in range(len(nums)-1,-1,-1):
            k = temp ^ val
            res.append(k)
            temp ^= nums[i]
        return res
        