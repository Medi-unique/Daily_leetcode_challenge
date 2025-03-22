class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {v:{v} for v in range(n)}
        for v,u in edges:
            g[v].add(u)
            g[u].add(v)
        
        return sum(len(q)==f for q,f in Counter(map(frozenset,g.values())).items())