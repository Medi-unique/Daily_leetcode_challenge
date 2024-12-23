from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        adj = defaultdict(list)
        self.comp = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            total = values[node]
            for neighbor in adj[node]:
                if neighbor != parent:
                    total += dfs(neighbor, node)
            
            if total % k == 0:
                self.comp += 1
                return 0
            return total % k

        dfs(0, -1)
        return self.comp