class Solution:
    def numTilings(self, n: int) -> int:
        generated = [1, 1, 2]
        if n < 3:
            return generated[n]
        for i in range(3, n+1):
            generated[2], generated[1], generated[0] = ((generated[2] * 2) + generated[0]) % ((10**9) + 7), generated[2], generated[1]
        return generated[-1]