from itertools import accumulate

class Solution:
    def maximumTripletValue(self, xs: List[int]) -> int:
        suf = list(accumulate(xs[::-1], max))[::-1]
        best, pre = 0, xs[0]
        for x, s in zip(xs[1:-1], suf[2:]):
            best = max(best, (pre - x) * s)
            pre = max(pre, x)
        return best