class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[]
        heapq.heapify(heap)
        for i in range(len(gifts)):
            heapq.heappush(heap,(-1*gifts[i]))
        for i in range(k):
            val=heapq.heappop(heap)
            val=-1*val
            heapq.heappush(heap,(-1*(floor(sqrt(val)))))
        ans=sum(heap)*-1
        return ans
        