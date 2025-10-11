'''https://leetcode.com/problems/distribute-candies-among-children-i/'''

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(limit, n) + 1):
            for j in range(min(limit, n - i) + 1):
                k = n - i - j
                if 0 <= k <= limit:
                    res += 1
        return res
