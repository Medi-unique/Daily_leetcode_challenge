class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def rec(s, d = set()):
            if not s:
                return len(d)
            ans = 0
            for i in range(1, len(s)+1):
                if s[:i] not in d and len(d)+len(s)-i >= ans:
                    ans = max(ans, rec(s[i:], d | {s[:i]}))
            return ans
        return rec(s)