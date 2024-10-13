class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        from sortedcontainers import SortedList
        k = len(nums)
        sl = SortedList(key=lambda x: (x[0], len(nums[x[1]]) - x[2]))
        l, r = -1e5-1, 1e5+1   
        mx_val = -1e5-1
        for i in range(k):
            sl.add((nums[i][0], i, 0))
            mx_val = max(mx_val, nums[i][0])
        
        while len(sl) == k:
            mn_val, i, j = sl.pop(0)
            if mx_val - mn_val < r - l:
                l, r = mn_val, mx_val
            if j + 1 < len(nums[i]):
                next_val = nums[i][j+1]
                sl.add((next_val, i, j+1))
                mx_val = max(mx_val, next_val)
        
        return [l, r]