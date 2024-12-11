class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        events = []
        for num in nums:
            events.append((num - k, 1))
            events.append((num + k + 1, -1))
        events.sort()
        max_beauty = 0
        current_overlap = 0
        for _, event_type in events:
            current_overlap += event_type
            max_beauty = max(max_beauty, current_overlap)
        
        return max_beauty