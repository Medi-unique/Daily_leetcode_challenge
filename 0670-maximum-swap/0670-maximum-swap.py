class Solution:
    from collections import defaultdict
    def maximumSwap(self, num: int) -> int:
        



        nums = str(num)
        start = 0
        stack = []

        for v in range(len(nums)):
            if not stack or int(nums[v]) <= stack[-1]:
                stack.append(int(nums[v]))
            else:
                start = v
                break

        swap = [float('-inf'), -1]

        for n in range(start,len(nums)):

            if int(nums[n]) >= swap[0]:
                swap[0] = int(nums[n])
                swap[1] = n
            
        
        res = list(nums)

        for n in range(swap[1]):
            if swap[0] > int(res[n]):
                res[swap[1]] = res[n]
                res[n] = str(swap[0])
                return (int("".join(res)))
                
        
        return num











        