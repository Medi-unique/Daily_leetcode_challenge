class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = max(ranks) * (cars**2)

        while left < right:
            t = (left + right) // 2
            n = 0

            for r in ranks:
                n += int((t/r)**0.5)
            
            if n >= cars:
                right = t
            else:
                left = t + 1
        return left