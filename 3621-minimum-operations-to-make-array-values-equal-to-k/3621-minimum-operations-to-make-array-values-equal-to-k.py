class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        check=set(nums)
        if min(check) < k:
            return -1
        if k in check:
            return len(check)-1
        else: return len(check)