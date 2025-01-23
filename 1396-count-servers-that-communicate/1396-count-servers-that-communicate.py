class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]: 
                    r, c = 0, 0
                    row = 0
                    col = 0
                    while c < n or r < m:
                        if c < n:
                            if grid[i][c] == 1:
                                col += 1
                            if col == 2:
                                cnt += 1
                                break
                            c += 1
                        else:
                            if grid[r][j] == 1:
                                row += 1
                            if row == 2:
                                cnt += 1
                                break
                            r += 1
        return cnt