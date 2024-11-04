class Solution:
    def compressedString(self, word: str) -> str:
        
        i = 0
        j = 1
        occurence = 1
        n = len(word)
        out = ''
        while j < n:

            while j < n and  word[j] == word[j - 1] and occurence < 9:
                occurence += 1
                j += 1

            out += str(occurence) + word[i] 
            occurence = 1
            i = j
            j += 1
            
        if j == n:
            out += str(1) + word[i]
        return out