class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)

        maxValue = [0] * n
        maxValue[-1] = events[-1][2]
        for i in range(n - 2, -1, -1):
            maxValue[i] = max(maxValue[i + 1], events[i][2])

        result = 0

        for i in range(n):
            currValue = events[i][2]
            result = max(result, currValue)

            lo, hi, nextEvent = i + 1, n - 1, -1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if events[mid][0] > events[i][1]:
                    nextEvent = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            if nextEvent != -1:
                result = max(result, currValue + maxValue[nextEvent])

        return result