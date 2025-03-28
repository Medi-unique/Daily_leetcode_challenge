from heapq import heappush, heappop

class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        m, n = len(grid), len(grid[0])
        ans = [0] * len(queries)
        sortedQ = sorted([(val, i) for i, val in enumerate(queries)])
        vis = [[False] * n for _ in range(m)]
        
        pq = []
        heappush(pq, (grid[0][0], 0, 0))
        vis[0][0] = True
        points = 0

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for qVal, qIdx in sortedQ:
            while pq and pq[0][0] < qVal:
                _, r, c = heappop(pq)
                points += 1
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if 0 <= x < m and 0 <= y < n and not vis[x][y]:
                        heappush(pq, (grid[x][y], x, y))
                        vis[x][y] = True
            ans[qIdx] = points
        return ans