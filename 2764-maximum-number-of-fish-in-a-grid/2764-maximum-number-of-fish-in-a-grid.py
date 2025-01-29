class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        parent={}
        size={}
        dir=[[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(m):
            for j in range(n):
                parent[(i,j)]=(i,j)
                size[(i,j)]=(i,j)
        def find(n):
            while n != parent[n]:
                parent[n]=parent[parent[n]]
                n=parent[n]
            return n
        def union(n1,n2):
            p1=find(n1)
            p2=find(n2)
            if p1!=p2:
                if size[p1]>size[p2]:
                    parent[p2]=p1
                    size[p1]+=size[p2]
                else:
                    parent[p1]=p2
                    size[p2]+=size[p1]
        def get_groups():
            groups=defaultdict(list)
            for i in range(m):
                for j in range(n):
                    p=find((i,j))
                    groups[p].append(grid[i][j])
            return groups
                
        for r in range(m):
            for c in range(n):
                if grid[r][c]!=0:
                    for i,j in dir:
                        nr =i+r
                        nc =j+c
                        if 0<= nr<m and 0<= nc < n and grid[nr][nc] !=0:
                            union((r,c),(nr,nc))
        final=get_groups()
        res=0
        for val in final.values():
            res=max(res,sum(val))
      
        return res




        