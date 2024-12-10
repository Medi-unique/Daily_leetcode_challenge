class Solution:
    def maximumLength(self, s: str) -> int:
        
        s = s + '#'

        cnt = defaultdict(list)
        prev, x = s[0], 1

        for ch in s[1:]:
            if ch == prev:
                x += 1
            else:
                cnt[prev].append(x)
                x = 1
            prev = ch


        best = 0
        for v in cnt.values():
            
            sv = sorted(v)
            
            if len(v) >= 2:
                a, b = sv[-1], sv[-2]

                best = max(best, min(b, a - 1))

                best = max(best, b - 1, a - 2)

                if len(v) >= 3:
                    best = max(best, sv[-3])

            else:
                best = max(best, v[0] - 2)
            
        return best if best else -1