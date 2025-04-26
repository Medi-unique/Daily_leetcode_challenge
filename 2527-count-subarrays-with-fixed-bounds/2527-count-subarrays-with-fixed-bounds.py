class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        minl=-1
        maxl=-1
        ans=0
        largest=-1
        for i,num in enumerate(nums):
            if num<minK or num>maxK:
                largest=i
            if num==minK:
                minl=i
            if num==maxK:
                maxl=i
            ans=ans+max(0,min(minl,maxl)-largest)
        return ans
            
            


            
        

        