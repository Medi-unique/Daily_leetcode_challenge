class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num=list(map(str,nums))
        def mycmp(first,second):
            if first+second>second+first:
                return 1
            elif first+second<second+first:
                return -1
            else:
                return 0
        res=sorted(num,key=cmp_to_key(mycmp),reverse=True)
        
        return ''.join(res).lstrip('0') or '0'

        