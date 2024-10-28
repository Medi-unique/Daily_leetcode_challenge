class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_ = set()
        for i in nums:
            set_.add(i)


        max_ = float('-inf')
        for num in nums:
            len_=1
            square_=num

            while square_*square_ <= float('inf') and (square_*square_) in set_:
                len_+=1
                square_=square_*square_

            max_ = max(len_, max_)

        
        return -1 if max_==1 else max_
        