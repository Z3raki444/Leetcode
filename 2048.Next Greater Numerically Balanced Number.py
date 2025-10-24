'''https://leetcode.com/problems/next-greater-numerically-balanced-number/description/'''

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x: int) -> bool:
            s = str(x)
            for d in set(s):
                if s.count(d) != int(d):
                    return False
            return True
        
        while True:
            n += 1
            if is_balanced(n):
                return n