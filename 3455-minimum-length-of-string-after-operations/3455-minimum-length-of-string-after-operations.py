class Solution:
    def minimumLength(self, s: str) -> int:
        arr = [0] * 26
        
        for ch in s:
            arr[ord(ch) - ord('a')] += 1
        
        for i in range(26):
            while arr[i] >= 3:
                arr[i] -= 2
        
        length = sum(arr)
        
        return length