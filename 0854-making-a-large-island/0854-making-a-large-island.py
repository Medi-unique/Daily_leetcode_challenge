class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        hash_map = {}

        def get_island():
            visit = {}
            area = []
            def dfs(i, j):
                nonlocal area
                visit[(i, j)] = True
                area.append((i, j))
                for dx, dy in d:
                    ni, nj = i + dx, j + dy
                    if ni >= 0 and ni < n and nj >= 0 and nj < m and (ni, nj) not in visit and grid[ni][nj] == 1:
                        dfs(ni, nj)
            
            ans = 0
            for i in range(n):
                for j in range(m):
                    if (i, j) not in visit and grid[i][j] == 1:
                        area = []
                        dfs(i, j)
                        for indx in area:
                            hash_map[indx] = (len(area), (i, j))
                        ans = max(ans, len(area))
            return ans
            
        
        ans = get_island()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    area = 1
                    entry = []
                    for dx, dy in d:
                        ni, nj = i + dx, j + dy
                        if ni >= 0 and ni < n and nj >= 0 and nj < m and grid[ni][nj] == 1:
                            if hash_map[(ni, nj)][1] not in entry:
                                area += hash_map[(ni, nj)][0]
                                entry.append(hash_map[(ni, nj)][1])

                    ans = max(ans, area)
        return ans

        