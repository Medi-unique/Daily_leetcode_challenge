class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers = set()

        for p, v in edges:
            losers.add(v)
        
        answer = []
        for team in range(n):
            if team not in losers:
                answer.append(team)
        
        return answer[0] if len(answer) == 1 else -1


        