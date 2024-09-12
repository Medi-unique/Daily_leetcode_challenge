class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        ele=set(allowed)
        for word in words:
            if all(char in ele for char in word):
                count=count+1

                    
        return count

        