class Solution(object):
    def resultsArray(self, nums, k):
        n = len(nums)

        if k == 1:
            return nums

        ans = []
        
        i, consecutiveSize = 1, 1
        
        while i < n:
            if nums[i] - 1 == nums[i - 1]:
                consecutiveSize += 1
            else:
                consecutiveSize = 1
            
            if i >= k - 1:
                if consecutiveSize >= k:
                    ans.append(nums[i])
                else:
                    ans.append(-1)
            
            i += 1
        
        return ans