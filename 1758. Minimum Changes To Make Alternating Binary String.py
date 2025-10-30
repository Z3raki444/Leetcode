'''https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/'''

class Solution:
    def minOperations(self, s: str) -> int:
        a = b = 0

        for i in range(len(s)):
            if s[i] != str(i % 2):
                a += 1
            else:
                b += 1

        return min(a, b)
