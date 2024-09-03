class Solution:
    def getLucky(self, s: str, k: int) -> int:
        check=''
        for l in s:
            check += str((ord(l)-ord('a')+1))
        num=sum(int(w) for w in check)
        for _ in range(k-1):
            num=sum(int(w) for w in str(num))
        return num

        