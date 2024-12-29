class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7  # Modulo for the result
        wl = len(words[0])  # Length of each word
        tl = len(target)    # Length of the target string

        # Initialize a DP array to track the number of ways to form each prefix of the target
        track = [0] * tl
        freq = [[0] * 26 for _ in range(wl)]

        # Precompute character frequencies for each position
        for word in words:
            for i in range(wl):
                freq[i][ord(word[i]) - ord('a')] += 1

        # Iterate over each position in the words
        for i in range(wl):
            temp = track[:]
            for j in range(tl):
                target_index = ord(target[j]) - ord('a')
                freqi = freq[i][target_index]
                if freqi > 0:  # Only update if the character exists
                    if j == 0:
                        temp[j] = (temp[j] + freqi) % MOD
                    elif track[j - 1] > 0:
                        temp[j] = (temp[j] + track[j - 1] * freqi) % MOD
            track = temp

        return track[tl - 1]