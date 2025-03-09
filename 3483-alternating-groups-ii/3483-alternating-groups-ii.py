class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        mask = (1 << k) - 1  
        state_one = 0
        state_two = 0
        x = 0
        curr = 0
        for i in range(-k, 0):
            state_one = (state_one << 1) | x
            x ^= 1
            state_two = (state_two << 1) | x
            curr = (curr << 1) | colors[i]

        cnt = 0
        for i in range(len(colors)):
            curr = ((curr << 1) | colors[i]) & mask
            if curr == state_one or curr == state_two:
                cnt += 1
        return cnt