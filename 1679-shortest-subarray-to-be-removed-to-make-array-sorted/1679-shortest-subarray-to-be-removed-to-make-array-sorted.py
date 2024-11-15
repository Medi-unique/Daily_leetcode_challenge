class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)
        right=n-1
        while (right>0 and arr[right-1]<=arr[right]):
            right-=1
    
        left=0
        shortest=right

        while ((left==0 or arr[left]>=arr[left-1]) and left<right and left<n-1):
            while (right<=n-1 and arr[left]>arr[right]):
                right+=1
                
            if right==n:
                shortest=min(shortest,right-left-1)

            shortest=min(shortest,right-left-1)
        

            left+=1
    
        return shortest