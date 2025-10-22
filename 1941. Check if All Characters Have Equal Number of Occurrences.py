'''https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/'''

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}

        for n in s:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        freq = set(freq.values())
        if len(freq) == 1:
            return True
        else:
            return False
    