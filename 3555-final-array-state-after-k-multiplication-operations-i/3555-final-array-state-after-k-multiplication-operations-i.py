class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[[val,i] for i,val in enumerate(nums)]
        heapq.heapify(heap)
        for i in range(k):
            val=heapq.heappop(heap)
            val[0]*=multiplier
            heapq.heappush(heap,val)
        arr=[0]*len(nums)
        for val in heap:
            arr[val[1]]=val[0]
        return arr