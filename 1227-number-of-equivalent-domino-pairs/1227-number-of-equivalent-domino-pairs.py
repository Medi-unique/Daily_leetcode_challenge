class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        check=Counter()
        ans=0
        for a,b in dominoes:
            key = tuple(sorted((a, b)))
            check[key] += 1
        for v in  check.values():
            if v>1:
                ans+= v*(v-1)//2
        return ans

