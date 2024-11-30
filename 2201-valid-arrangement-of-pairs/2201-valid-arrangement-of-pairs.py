class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        degree = defaultdict(int)

        for u, v in pairs:
            graph[u].append(v)
            degree[u] += 1
            degree[v] -= 1

        startNode = pairs[0][0]

        for node in degree:
            if degree[node] == 1:
                startNode = node    
                break
        path = []

        def dfs(node):
            while graph[node]:
                next = graph[node].pop()
                dfs(next)
                path.append([node, next])

        dfs(startNode)
        return path[::-1]