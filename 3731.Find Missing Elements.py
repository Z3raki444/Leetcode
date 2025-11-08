'''https://leetcode.com/problems/find-missing-elements/description/'''

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        missing = []
        nums_set = set(nums)

        num = min(nums)
        while num <= max(nums):
            if num not in nums_set:
                missing.append(num)
            num += 1
        
        return missing
