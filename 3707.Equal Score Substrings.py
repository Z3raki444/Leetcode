'''https://leetcode.com/problems/equal-score-substrings/description/'''

class Solution:
    def scoreBalance(self, s: str) -> bool:
        if len(s) < 2:
            return False

        def score(ch: str) -> int:
            return ord(ch) - ord('a') + 1

        total = sum(score(ch) for ch in s)
        left = 0
 
        for i in range(1, len(s)):
            left += score(s[i - 1])
            if left * 2 == total:
                return True
        return False
