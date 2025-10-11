'''https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)
        nums_set = set(nums)
        result = []

        for i in range(1, n + 1):
            if i not in nums_set:
                result.append(i)

        return result

