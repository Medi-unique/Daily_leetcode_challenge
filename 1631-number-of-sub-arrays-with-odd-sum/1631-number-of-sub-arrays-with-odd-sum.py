class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefixSum = 0
        oddSumCount, evenSumCount = 0, 0
        ans = 0
        
        for num in arr:
            prefixSum += num
            
            if prefixSum % 2 == 1:
                ans += 1 + evenSumCount
                oddSumCount += 1
            else:
                ans += oddSumCount
                evenSumCount += 1
                
        return int(ans % (1e9 + 7))