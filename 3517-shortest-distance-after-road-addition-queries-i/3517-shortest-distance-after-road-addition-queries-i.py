class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        adj = defaultdict(list)

        for i in range(n-1):
            adj[i].append((i+1, 1))
        


        def bfs():
            heap = []
            heapq.heappush(heap, (0, 0))
            distances = [float('inf')] * n
            distances[0] = 0
            visited = set()

            while heap:
                dist, city = heapq.heappop(heap)

                if city in visited:
                    continue
                
                visited.add(city)
                
                for neigh, neigh_dist in adj[city]:
                    if dist + neigh_dist < distances[neigh]:
                        distances[neigh] = dist + neigh_dist
                        heapq.heappush(heap, (distances[neigh], neigh))
                
            if distances[n-1] != float("inf"):
                return distances[n-1]
            return -1

        ans = []
        d = n-1
        for query in queries:
            adj[query[0]].append((query[1], 1))
            ans.append(bfs())

        return ans