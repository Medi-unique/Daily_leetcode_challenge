class Solution(object):
    def dfs(self, grid, visited, i, j, m, n, islands):
        # mark area as visited
        visited[i][j] = True
        # add coordinate to the array
        islands.append([i, j])

        # travel left, right, up, or down to explore
        if i + 1 < m and not visited[i + 1][j] and grid[i + 1][j] == 1:
            self.dfs(grid, visited, i + 1, j, m, n, islands)
        if i - 1 >= 0 and not visited[i - 1][j] and grid[i - 1][j] == 1:
            self.dfs(grid, visited, i - 1, j, m, n, islands)
        if j + 1 < n and not visited[i][j + 1] and grid[i][j + 1] == 1:
            self.dfs(grid, visited, i, j + 1, m, n, islands)
        if j - 1 >= 0 and not visited[i][j - 1] and grid[i][j - 1] == 1:
            self.dfs(grid, visited, i, j - 1, m, n, islands)
        # return coordinates that make up a single island
        return islands

    def minDays(self, grid):
        m = len(grid)
        if m != 0:
            n = len(grid[0])

        island = 0
        islands = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    island += 1
                    islands.append(self.dfs(grid, visited, i, j, m, n, []))

        if island == 0 or island > 1:
            return 0

        for cell in islands:
            for s, k in cell:
                grid[s][k] = 0

                new_island = 0

                visited = [[False for _ in range(n)] for _ in range(m)]
                for i in range(m):
                    for j in range(n):
                        if not visited[i][j] and grid[i][j] == 1:
                            new_island += 1
                            self.dfs(grid, visited, i, j, m, n, [])
                grid[s][k] = 1
                if island != new_island:
                    return 1

        return 2