class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def check(x,n):
            if n==0: return 1
            if n%2 == 0:
                return check( (x*x %(10**9 + 7)), n//2)
            else:
                return x * check(x ,n-1)
        return (check(5, n-(n//2))*check(4,n//2)) %(10**9 +7)

            

        