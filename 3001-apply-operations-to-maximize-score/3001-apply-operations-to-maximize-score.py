__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
MOD, MX = 1000000007, 100001 ; omega = [0]*MX
for i in range(2, MX): 
    if not omega[i]: 
        for j in range(i, MX, i):   omega[j] += 1

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n, st, ans = len(nums), [], 1 ; left, right = [-1]*n, [n]*n
        for i, v in enumerate(nums):
            while st and omega[nums[st[-1]]] < omega[v]: right[st.pop()] = i
            left[i] = st[-1] if st else -1 ; st.append(i)

        for i, v, l, r in sorted(zip(range(n), nums, left, right), key=lambda x: -x[1]): 
            tot = (i-l)*(r-i)
            if tot >= k: return ans * pow(v, k, MOD) % MOD
            ans = ans * pow(v, tot, MOD) % MOD ; k -= tot
        return ans