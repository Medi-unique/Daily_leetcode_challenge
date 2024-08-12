class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = []        
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]