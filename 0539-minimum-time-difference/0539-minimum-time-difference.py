class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertToMinutes(time: str) -> int:
            h, m = map(int, time.split(':'))
            return h * 60 + m
        
        minutes = [convertToMinutes(time) for time in timePoints]
        minutes.sort()
        
        min_diff = float('inf')
        n = len(minutes)
        
        for i in range(1, n):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        min_diff = min(min_diff, (1440 - minutes[-1] + minutes[0]))
        
        return min_diff
