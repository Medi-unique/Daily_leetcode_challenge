class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for a,b in prerequisites: 
            graph[b].append(a)

        cache = {}
        def dfs(node,dest): 
            if node==dest:
                return True

            if (node,dest) in cache:
                return cache[(node,dest)]

            cache[(node,dest)] = True
            for nei in graph[node]:
                if dfs(nei,dest):
                    return True

            cache[(node,dest)] = False
            return False  

        res = []
        for u,v in queries: 
            res.append(dfs(v,u))

        return res