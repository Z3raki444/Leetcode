'''https://leetcode.com/problems/find-the-duplicate-number/description/'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> List[int]:
        result = []
        seen = set()

        for n in nums:
            if n in seen:
                result.append(n)
            seen.add(n)

        return result[0]


