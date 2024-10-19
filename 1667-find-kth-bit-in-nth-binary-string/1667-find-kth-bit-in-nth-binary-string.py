class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s1='0'
        for i in range(1,n+1):
            cur=''
            for l in s1 :
                if l=='0':
                    cur+='1'

                else:
                 cur+= '0'
            cur=''.join(reversed(cur))
            s1=s1+'1'+cur
        return s1[k-1]
        