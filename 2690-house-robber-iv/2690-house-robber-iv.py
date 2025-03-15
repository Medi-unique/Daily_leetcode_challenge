class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minH = min(nums)
        maxH = max(nums)
        def money(capability):
            steal, j = 0, 0
            while j < n and steal < k:
                if nums[j] <= capability:
                    steal += 1
                    j += 1
                j += 1
            return steal >= k
        
        left, right = minH, maxH
        while left < right:
            mid = (left + right) >> 1
            if money(mid):
                right = mid
            else:
                left = mid + 1
        return left
