class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        distinct = 0
        freq, colors = {}, {}
        res = []
        for x, y in queries:
            freq[y] = freq.get(y, 0) + 1
            if freq[y] == 1:
                distinct += 1
            if x in colors:
                freq[colors[x]] -= 1
                if freq[colors[x]] == 0:
                    distinct -= 1
            colors[x] = y
            res.append(distinct)
        return res