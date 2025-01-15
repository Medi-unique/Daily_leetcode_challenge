class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_count = bin(num1).count('1')
        num2_count = bin(num2).count('1')
        
        while num1_count < num2_count:
            num1 |= num1 + 1
            num1_count += 1
        
        while num1_count > num2_count:
            num1 &= num1 - 1
            num1_count -= 1
        
        return num1