class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans=0
        for w in words:
            if len(w)>=len(pref):
                if pref== w[:len(pref)]:
                    ans+=1
        return ans