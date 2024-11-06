class Solution:
    def setbit(self, num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    def canSortArray(self, nums):
        n = len(nums)
        
        for i in range(n - 1):
            for j in range(n - 1):
                if nums[j] > nums[j + 1] and self.setbit(nums[j]) == self.setbit(nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        return nums == sorted(nums)