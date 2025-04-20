class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        res=0
        for key,value in count.items():
            if key==0:
                res += value

            elif value<= key+1:
                res+=key+1
            else:
                res+= (ceil(value/(key+1)) * (key+1))
        return res


        