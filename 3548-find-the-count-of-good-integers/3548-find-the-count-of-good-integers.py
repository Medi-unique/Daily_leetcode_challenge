class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1: return 9//k
        ans = 0 
        half = n//2
        valid = set()
        for x in range(1, pow(10, half)): 
            part = str(x).zfill(half)
            if not part.endswith('0'): 
                if n&1: cands = [part[::-1] + str(mid) + part for mid in range(0, 10)]
                else: cands = [part[::-1] + part]
                for cand in cands: 
                    if int(cand) % k == 0: 
                        key = "".join(sorted(cand))
                        valid.add(key)
                        
        def multinom(vals): 
            ans = k = 1
            for x in vals: 
                for i in range(1, x+1): 
                    ans *= k
                    ans //= i
                    k += 1
            return ans 
        
        for key in valid: 
            freq = Counter(key)
            val = multinom(freq.values())
            if freq['0']: 
                freq['0'] -= 1
                val -= multinom(freq.values())
            ans += val 
        return ans 