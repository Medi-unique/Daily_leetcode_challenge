class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1)%2==0 and len(nums2)%2!=0:
            a=0
            for i in nums1:
                a=a^i
            return a

        if len(nums2)%2==0 and len(nums1)%2!=0:
            a=0
            for i in nums2:
                a=a^i
            return a

        if len(nums1)%2==0 and len(nums2)%2==0:
            return 0

        if len(nums1)%2!=0 and len(nums2)%2!=0:
            a=0
            for i in nums1:
                a=a^i
            for i in nums2:
                a=a^i
            return a
        


        