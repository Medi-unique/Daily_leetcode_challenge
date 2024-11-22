class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)
        ans = 0
        for row in matrix:
            if row[0] == 1:
                row = [1^bit for bit in row]
            count[tuple(row)]+=1
            ans=max(count[tuple(row)],ans)
        return ans

        