class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0]) 
        U=sum(grid[0])-grid[0][0] 
        D=0
        Robot2=U 

        for i in range(1, n): 
            U-=grid[0][i] 
            D+=grid[1][i-1]

            P=max(U, D)
            Robot2=min(Robot2, P)

        return Robot2