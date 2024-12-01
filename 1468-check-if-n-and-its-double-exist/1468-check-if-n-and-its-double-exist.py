class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for val in arr:
            if val*2 in arr:
                if val==0 and arr.count(0)==1:
                    continue
                return True
        return False
        