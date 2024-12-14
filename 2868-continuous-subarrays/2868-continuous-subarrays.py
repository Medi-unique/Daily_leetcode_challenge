class Solution:
    def continuousSubarrays(self, nums):
        n = len(nums)
        total = 0
        left = 0
        dict1 = defaultdict(int)
        

        for right in range(n):
            dict1[nums[right]] += 1

            while max(dict1.keys()) - min(dict1.keys()) > 2:
                dict1[nums[left]] -= 1

                if dict1[nums[left]] == 0:
                    del dict1[nums[left]]

                left += 1

            total += right-left+1

        return total



