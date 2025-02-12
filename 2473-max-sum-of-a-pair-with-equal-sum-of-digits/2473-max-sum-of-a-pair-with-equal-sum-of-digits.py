class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        count=defaultdict(list)
        for num in nums:
            c=str(num)
            s=0
            for l in c:
                s+=int(l)
            count[s].append(num)
        ans=0
        for val in count.values():
            if len(val)>=2:
                val.sort()
                ans=max(ans,sum(val[len(val)-2:]))
        return ans if ans >0 else -1


        