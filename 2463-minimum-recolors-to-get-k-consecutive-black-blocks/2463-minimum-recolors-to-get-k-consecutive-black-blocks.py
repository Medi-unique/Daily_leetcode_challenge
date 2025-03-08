class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans= float("inf")
        ans=min(ans,blocks[:k].count('W'))

        for i in range(1,len(blocks)-k+1):
            ans=min(ans,blocks[i:i+k].count('W'))
        return ans
    
        