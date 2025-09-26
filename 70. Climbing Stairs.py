'''https://leetcode.com/problems/climbing-stairs/'''

import math


class Solution:
    def climbStairs(self, n: int) -> int:
        total = 0
        for k in range(n // 2 + 1):              # k = number of 2-steps
            total += math.comb(n - k, k)         # choose positions of the k twos
        return total