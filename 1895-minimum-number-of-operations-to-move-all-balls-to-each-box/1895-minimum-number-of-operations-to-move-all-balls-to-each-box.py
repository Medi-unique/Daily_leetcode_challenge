class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes=list(boxes)
        
        res=[]
        for i in range(len(boxes)):
            total=0
            for j,n in enumerate(boxes):
                
                if n== '1':
                    total+=abs(j-i)
                
            res.append(total)
        return res
                    
                
        