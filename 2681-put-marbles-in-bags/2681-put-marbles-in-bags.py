class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        t=[weights[i]+weights[i+1] for i in range(len(weights)-1)]
        t.sort()
        return sum(t[1-k:])-sum(t[:k-1]) if k>1 else 0