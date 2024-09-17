class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans=set()
        check=s1+' '+s2
        check=check.split()
        for val in check:
            if check.count(val)==1:
                ans.add(val)
        return list(ans)

        