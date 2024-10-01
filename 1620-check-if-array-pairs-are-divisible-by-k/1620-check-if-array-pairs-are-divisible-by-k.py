from collections import Counter
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        store = Counter()

        for ele in arr:
            rem = ele%k
            store[rem] +=1
        
        for ele in arr:
            rem = ele%k

            if rem ==0 or (2*rem ==k):
                if store[rem]%2 !=0:
                    return False
            
            elif store[rem] != store[k-rem]:
                return False

        return True 

        