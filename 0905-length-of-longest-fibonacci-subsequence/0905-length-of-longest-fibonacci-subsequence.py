class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_length = 0
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        value_to_index = {value: index for index, value in enumerate(arr)}
        
        for third_index in range(2, n):
            third_value = arr[third_index]
            for second_index in range(third_index - 1, 0, -1):
                second_value = arr[second_index]
                if second_value * 2 <= third_value:
                    break
                first_value = third_value - second_value
                first_index = value_to_index.get(first_value, -1)
                if first_index >= 0:
                    dp[second_index][third_index] = max(dp[first_index][second_index] + 1, 3)
                    max_length = max(max_length, dp[second_index][third_index])
        
        return max_length