class Solution:
    def countPrefixSuffixPairs(self, words):
        def is_prefix_suffix(w1, w2):
            l1, l2 = len(w1), len(w2)
            if l1 > l2:
                return False
            if w1 != w2[:l1]:
                return False
            if w1[::-1] != w2[::-1][:l1]:
                return False
            return True

        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if is_prefix_suffix(words[i], words[j]):
                    count += 1
        return count