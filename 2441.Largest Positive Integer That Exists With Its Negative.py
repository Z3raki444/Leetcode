'''https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/'''

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        result = []

        for num in nums:
            if -num in nums:
                result.append(abs(num))

        if result:
            return max(result)
        else:
            return -1