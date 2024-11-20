class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n=len(s)
        c_a=c_b=c_c=0
        for char in s:
            if char=="a":
                c_a+=1
            elif char=="b":
                c_b+=1
            elif char=="c":
                c_c+=1
        if (c_a<k or c_b<k or c_c<k):
            return -1 
        delete=0
        l=0 #left 
        r=0  #right
        while r<n:
            if s[r]=="a":
                c_a-=1
            elif s[r]=="b":
                c_b-=1
            else:
                c_c-=1

            while (l<=r) and (c_a<k or c_b<k or c_c<k):
                if s[l]=="a":
                    c_a+=1
                elif s[l]=="b":
                    c_b+=1
                else:
                    c_c+=1
                l+=1 
            delete=max(delete,r-l+1)
            r+=1 

        return n-delete 