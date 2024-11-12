from typing import List
import bisect

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        
        beauty = []
        best = 0
        for p, b in items:
            best = max(best, b)
            beauty.append((p, best))

        ans = []
        for q in queries:
            i = bisect.bisect_right(beauty, (q, float('inf'))) - 1
            if i >= 0:
                ans.append(beauty[i][1])
            else:
                ans.append(0)
        
        return ans
