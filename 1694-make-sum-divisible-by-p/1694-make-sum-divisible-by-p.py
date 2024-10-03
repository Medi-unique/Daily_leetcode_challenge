class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total % p == 0:
            return 0

        cur_sum = 0
        prefix_sum = []
        for i in range(len(nums)):
            cur_sum += nums[i]
            prefix_sum.append(cur_sum)

        tracker = {
            0: -1
        }
        res = float('inf')
        for j in range(len(prefix_sum)):
            if ((prefix_sum[j] % p) - (total % p)) % p in tracker:
                res = min(res, j - tracker[((prefix_sum[j] % p) - (total % p)) % p])
            tracker[prefix_sum[j] % p] = j

        return res if res != len(nums) else -1