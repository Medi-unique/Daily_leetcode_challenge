import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        
        score = 0
        
        while k > 0:
            ele = -heapq.heappop(heap)
            score += ele
            
            heapq.heappush(heap, -math.ceil(ele / 3))
            k -= 1
        
        return score