class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count=Counter()
        for i in range(len(bills)):
            count[bills[i]]+=1
            if bills[i]==10:
                count[5]-=1
            elif bills[i]==20:
                if count[10]>0:
                    count[10]-=1
                else:
                    count[5]-=2
                count[5]-=1
            if count[5]<0:
                return False
        return True 
            


        