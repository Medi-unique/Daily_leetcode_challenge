class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        vowels=set(['a','e','i','o','u'])
        vstrings=[0]*n
        for i,w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                vstrings[i]=1
        prefix=[vstrings[0]]
        for i in range(1,n):
            prefix.append(prefix[-1]+vstrings[i])
        result=[]
        for l,r in queries:
            if l==0:
                result.append(prefix[r])
            else:
             result.append(abs(prefix[r]-prefix[l-1]))
        return result

        