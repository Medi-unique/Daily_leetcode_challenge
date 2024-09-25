class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        
        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
                current.prefix_count += 1  
        
        result = []
        for word in words:
            current = root
            score = 0
            for char in word:
                current = current.children[char]
                score += current.prefix_count 
            result.append(score)
        
        return result