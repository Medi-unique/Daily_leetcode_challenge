class Solution:
    def smallestNumber(self, s: str) -> str:
        
        return min(
            ''.join(p) for p in permutations('123456789'[:len(s)+1])
                if all((gt,lt)[q=='I'](*p[i:i+2]) for i,q in enumerate(s))
        )
        # check=''
        # for i in range(len(pattern)+1):
        #     check += str(i+1)

        # alll =list(permutations(check))
        # alll.sort()
        # for l in alll:
        #     for i in range(1,len(l)):
        #         if pattern[i-1]=='D' and int(l[i])>int(l[i-1]):
        #             continue
        #         elif pattern[i-1]=='I' and int(l[i])<int(l[i-1]):
        #             continue
        #     return l
        