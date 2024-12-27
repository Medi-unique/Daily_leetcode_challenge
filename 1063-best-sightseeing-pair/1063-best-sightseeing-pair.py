class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        add = [num + i for i,num in enumerate(values)]

        max_heap = [(-(num - i),i) for i,num in enumerate(values)]
        heapq.heapify(max_heap)

        res = 0

        for i,num in enumerate(add):

            while max_heap and max_heap[0][1] <= i:
                heapq.heappop(max_heap)
            
            if max_heap:
                res = max(res,num + -max_heap[0][0])
        
        return res