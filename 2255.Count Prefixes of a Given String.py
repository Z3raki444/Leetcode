'''https://leetcode.com/problems/count-prefixes-of-a-given-string/description/'''

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if s.startswith(word):
                count += 1
        return count