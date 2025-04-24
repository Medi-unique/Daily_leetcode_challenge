class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique= len(set(nums))
        count=Counter()
        left,size=0,len(nums)
        res=0

        for right , num in enumerate(nums):
            count[num]+=1
            while len(count)==unique:
                res += size - right
                count[nums[left]]-=1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                left +=1
        return res

        