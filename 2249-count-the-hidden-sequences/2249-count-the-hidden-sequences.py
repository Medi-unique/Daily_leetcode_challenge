class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        res = [0] * (n + 1)
        res[0] = upper

        for i in range(n):
            res[i + 1] = res[i] - differences[n - i - 1]

        good_mins = min(res) - lower + 1
        bad_max = max(res) - upper

        if good_mins - bad_max <= 0:
            return 0
        
        if bad_max > 0:
            return good_mins - bad_max
        
        return good_mins