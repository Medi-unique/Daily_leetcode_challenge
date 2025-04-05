from itertools import chain, combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        sumi=0
        for i in range(1 << n):
            sub=0
            for j in range(n):
                 if i & (1 << j):
                    sub ^= nums[j]
            sumi+=sub
        return sumi