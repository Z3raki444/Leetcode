'''https://leetcode.com/problems/find-all-duplicates-in-an-array/description/'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []

        for n in nums:
            if n in seen:
                result.append(n)
            else:
                seen.add(n)

        return result
