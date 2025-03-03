class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        great=[]
        equal=[]
        for n in nums:
            if n< pivot:
                less.append(n)
            elif  n> pivot:
                great.append(n)
            else:
                equal.append(n)
                
        
        return less+equal+great
        