class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(['0' if i == '1' else '1' for i in bin(num)[2:]]), 2)
        