class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # directions=[[1,0],[0,1],[-1,0],[0,-1]]
        # def inbound(r,c):
        #     return  0<= r <m and 0<= c < n
        # matrix=[]
        # for r in range(m):
        #     matrix.append([0]*n)
        # for i,val in enumerate(guards):
        #     matrix[val[0]][val[1]] = 'G'
        # for i,val in enumerate(walls):
        #     matrix[val[0]][val[1]]='W'
        # for r in range(m):
        #     for c in range(n):
        #         if matrix[r][c]=='G':
        #             for i,j in directions:
        #                 while inbound(r+i,c+j) and matrix[[r+i][c+j]] !='G' and matrix[[r+i][c+j]]!='W':
        #                     matrix[r+i][c+j]='X'
        # ans=0
        # for r in range(m):
        #     for c in range(n):
        #         if matrix[r][c]==0:
        #             ans+=1
        # return ans

       
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        
        matrix = [[0] * n for _ in range(m)]
        
        for r, c in guards:
            matrix[r][c] = 'G'
        for r, c in walls:
            matrix[r][c] = 'W'
        
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while inbound(nr, nc):
                    if matrix[nr][nc] in ('G', 'W'):  # Stop at guard or wall
                        break
                    if matrix[nr][nc] == 0:  # Only mark empty spaces
                        matrix[nr][nc] = 'X'
                    nr += dr
                    nc += dc
        
        # Count unguarded spaces
        ans = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:  # Empty and unguarded
                    ans += 1
        
        return ans
        
        