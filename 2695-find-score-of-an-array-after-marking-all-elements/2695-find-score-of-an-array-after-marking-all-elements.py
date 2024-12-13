class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap=[[nums[i],i] for i in range(len(nums))]
        heapq.heapify(heap)
        visited=set()
        score=0
        while len(heap)>0:
            val=heapq.heappop(heap)
            if val[1] in visited:
                continue
            score+=val[0]
            if val[1]>=1:
                visited.add(val[1]-1)
            if val[1]<len(nums)-1:
                visited.add(val[1]+1)
        return score

        