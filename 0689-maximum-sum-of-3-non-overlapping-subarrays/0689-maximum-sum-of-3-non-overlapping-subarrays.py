class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        sums = [sum(nums[i:i+k]) for i in range(n-k+1)]
        
        left = [0] * (n-k+1)
        right = [n-k] * (n-k+1)
        for i in range(1, n-k+1):
            if sums[i] > sums[left[i-1]]:
                left[i] = i
            else:
                left[i] = left[i-1]
            if sums[n-k-i] >= sums[right[n-k-i+1]]:
                right[n-k-i] = n-k-i
            else:
                right[n-k-i] = right[n-k-i+1]
        
        max_sum = float('-inf')
        res = [0, k, 2*k]
        
        for i in range(k, n-2*k+1):
            left_sum = sums[left[i-k]]
            right_sum = sums[right[i+k]]
            mid_sum = sums[i]
            total_sum = left_sum + mid_sum + right_sum
            
            if total_sum > max_sum:
                max_sum = total_sum
                res = [left[i-k], i, right[i+k]]
        
        return res