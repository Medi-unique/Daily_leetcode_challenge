import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1

        m, n = len(grid), len(grid[0])
        heap = [(0, 0, 0)]  
        visit = [[False] * n for _ in range(m)]  
        visit[0][0] = True  
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        while heap:
            t, r, c = heapq.heappop(heap)

            if (r, c) == (m - 1, n - 1):
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visit[nr][nc]:
                    wait = abs(grid[nr][nc] - t) % 2 == 0
                    new_t = max(grid[nr][nc] + wait, t + 1)

                    heapq.heappush(heap, (new_t, nr, nc))
                    visit[nr][nc] = True  
        return -1