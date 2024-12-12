class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()


        def unbound(r,c):
            return r<0 or r>=len(grid) or c<0 or c>=len(grid[0])

        def dfs(r,c):
            if unbound(r,c) or grid[r][c]=='0' or (r,c) in visited: return 
            

            visited.add((r,c))
            grid[r][c]='0'

            for cr,cc in dir:
                nr,nc=r+cr,c+cc
                dfs(nr,nc)
             

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island+=1
                    dfs(i,j)
        return island

        