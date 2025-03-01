
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left, right = 0, 1

        while right < N:
            if nums[left] == nums[right]:
                nums[left] = nums[left] * 2
                nums[right] = 0
            
                left = right + 1
                right = left + 1
            else:
                left += 1
                right += 1
        
        nums = [n for n in nums if n != 0]
        zeros = N - len(nums) 
        nums.extend([0] * zeros)

        return nums