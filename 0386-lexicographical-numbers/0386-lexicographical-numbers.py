class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        i = 1
        ans = []    
        for i in range(1,n+1):  
            ans.append(i)   
        
        ans.sort(key=str)   
        return ans