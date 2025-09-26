'''https://leetcode.com/problems/sqrtx/description/'''

class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while n * n <= x:
            n += 1
        return n - 1  
