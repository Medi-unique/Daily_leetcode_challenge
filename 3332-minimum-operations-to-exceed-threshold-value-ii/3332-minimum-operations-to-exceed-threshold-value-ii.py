class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans=0
        heapq.heapify(nums)
        while  len(nums) >1:
            x=heapq.heappop(nums)
            if  x >= k: break
            y=heapq.heappop(nums)
            val=min(x, y) * 2 + max(x, y)
            heapq.heappush(nums,val)
            ans+=1
        return ans




        