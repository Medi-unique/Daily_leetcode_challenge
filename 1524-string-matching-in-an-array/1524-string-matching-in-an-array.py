class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x:len(x))
        n=len(words)
        result=[]
        for i in range(n):
            for j in range(n-1,i,-1):
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
        
