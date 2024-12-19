class Solution:
    def maxChunksToSorted(self, a: List[int]) -> int:
        return sum(starmap(eq,enumerate(accumulate(a,max))))