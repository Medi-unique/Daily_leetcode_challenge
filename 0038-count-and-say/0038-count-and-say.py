class Solution:
    def countAndSay(self, n: int, res = '1') -> str:
        if n == 1:
            return res

        new_res = ''
        counts = 1

        for i in range(len(res) - 1):
            if res[i] == res[i + 1]:
                counts += 1
            else:
                new_res += str(counts) + res[i]
                counts = 1
        
        new_res += str(counts) + res[-1]

        return self.countAndSay(n - 1, new_res)