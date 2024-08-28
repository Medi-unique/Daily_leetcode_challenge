class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count = 0
        m,n = len(grid1),len(grid1[0])
        visited = set()
        dir =[(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(x,y):
            q = deque([(x,y)])
            visited.add((x,y))
            res = 1

            while q:
                x,y = q.popleft()

                if not grid1[x][y]:
                    res = 0

                for dx,dy in dir:
                    r,c = x+dx,y+dy
                    if 0<=r<m and 0<=c<n and grid2[r][c] and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))

            return res

        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and (i,j) not in visited:
                    count+=bfs(i,j)
                    
        return count
            