class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        u,l=0,0
        n=len(str1)
        m=len(str2)
        while u<n and l<m:
            if str1[u]==str2[l]  or (str2[l]=='a' and str1[u] =='z') or (ord(str2[l])-1)==ord(str1[u]):
                l+=1
            u+=1
        if l==m:
            return True
        else:
            return False