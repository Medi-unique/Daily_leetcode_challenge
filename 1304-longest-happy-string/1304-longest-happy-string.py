class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = []
        if a > 0:
            heapq.heappush(freq, (-a, 'a'))
        if b > 0:
            heapq.heappush(freq, (-b, 'b'))
        if c > 0:
            heapq.heappush(freq, (-c, 'c'))
        
        result = []
        
        while freq:
            first = heapq.heappop(freq)
            
            if len(result) >= 2 and result[-1] == result[-2] == first[1]:
                if not freq:
                    break  
                second = heapq.heappop(freq)
                result.append(second[1])
                second = (second[0] + 1, second[1])  
                if second[0] != 0:
                    heapq.heappush(freq, second)
                heapq.heappush(freq, first) 
            else:
                result.append(first[1])
                first = (first[0] + 1, first[1]) 
                if first[0] != 0:
                    heapq.heappush(freq, first)
        
        return ''.join(result)