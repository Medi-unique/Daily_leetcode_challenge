class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod=int(1e9+7)
        @cache
        def solve(count):
            if count==high:
                return 1
            base=1 if count>=low else 0
            if count+zero<=high:
                base=(base+solve(count+zero))%mod
            if count+one<=high:
                base=(base+solve(count+one))%mod
            return base
        return solve(0)