class Solution:
    def minimumSubarrayLength(self, a: List[int], k: int) -> int:
        res, z, p1 = inf, Counter(), 0
        for p2 in range(len(a)):
            z.update(i for i,c in enumerate(bin(a[p2])[:1:-1]) if c=='1')
            while p1<=p2 and sum(1<<i for i,f in z.items() if f)>=k:
                res = min(res, p2-p1+1)
                z.update({i:-1 for i,c in enumerate(bin(a[p1])[:1:-1]) if c=='1'})
                p1 += 1

        return res==inf and -1 or res