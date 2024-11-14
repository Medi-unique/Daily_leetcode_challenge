class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, 100000
        while l < r:
            mid = (l + r) // 2
            stores = n
            for quantity in quantities:
                stores -= (quantity + mid - 1) // mid
                if stores < 0: break
            if stores >= 0:
                r = mid
            else:
                l = mid + 1
        return r