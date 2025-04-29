class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        m=max(nums)
        c=0
        res=0
        for r in range(len(nums)):
            if nums[r]==m:
                c+=1
            while c >= k:
                if nums[l]==m:
                    c-=1
                l+=1
                
            res+=l
        return res

        