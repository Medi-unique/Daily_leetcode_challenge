class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1)==Counter(s2):
            c=0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    c+=1
            if c> 2: return False
            return True
        return False

        # check=set()
        # for i in range(len(s1)):
        #     if s1[i] != s2[i]:
        #         check.add(s1[i])
        #         check.add(s2[i])
        # if len(check)<=2:
        #         return True
        # return False

        