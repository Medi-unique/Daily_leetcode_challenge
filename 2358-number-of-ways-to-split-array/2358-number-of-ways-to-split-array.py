class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        right=sum(nums)
        left=0
        ans=0
        for i in range(n-1):
            right-=nums[i]
            left+=nums[i]
            if left>=right:
                ans+=1
        return ans
        # pref=[0]
        # ans=0
        # for i in range(n):
        #     pref.append(pref[-1]+pref[i])
        # pref=pref[1:]
        # for j in range(1,n):
        #     if pref[j-1]>=pref[-1]-pref[j]:
        #         ans+=1
        # return ans