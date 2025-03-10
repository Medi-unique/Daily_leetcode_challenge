class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        res = cons = left = cur = 0
        freq = defaultdict(int)
        vowel = 'aeiou'

        for ch in word:
            if ch in vowel:
                freq[ch] += 1
            else: 
                cons += 1
                cur = 0 

            while cons > k:
                if word[left] not in vowel:
                    cons -= 1
                elif freq[word[left]] == 1:
                    del freq[word[left]]
                else:
                    freq[word[left]] -= 1
                left += 1

            while len(freq) == 5 and cons == k:
                cur += 1
                if word[left] not in vowel:
                    cons -= 1
                elif freq[word[left]] == 1:
                    del freq[word[left]]
                else:
                    freq[word[left]] -= 1
                left += 1
            res += cur 
        return res

            