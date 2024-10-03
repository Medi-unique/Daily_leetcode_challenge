class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        total_sum = sum(nums)
        target_rem = total_sum % p
        
        if target_rem == 0:
            return 0 
            
        prefix_sum = 0
        prefix_sums = {0: -1}  
        min_length = len(nums)
        curr_rem = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            curr_rem = prefix_sum % p
            prev_rem = (curr_rem - target_rem + p) % p  
            
            if prev_rem in prefix_sums:
                min_length = min(min_length, i - prefix_sums[prev_rem])
            
            prefix_sums[curr_rem] = i
        
        return min_length if min_length < len(nums) else -1  

