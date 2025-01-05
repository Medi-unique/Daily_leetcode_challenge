class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        new=[0]*n
        ans=''
        for l,r,d in shifts:
            if d==0:
                new[l]-=1
                if r!=n-1:
                    new[r+1]+=1
            elif d==1:
                new[l]+=1
                if r!=n-1:
                    new[r+1]-=1
        pref=[new[0]]
        for i in range(1,len(new)):
            pref.append(pref[-1]+new[i])
        print(pref)
        for st,num in zip(s,pref):
            check=chr(((ord(st)-97+num)%26)+97)
            ans+=check
        return ans
    
        