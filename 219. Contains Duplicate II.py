'''https://leetcode.com/problems/contains-duplicate-ii/description/'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        i = 0
        while i < len(nums):
            num = nums[i]
            if num in seen and i- seen[num] <= k:
                return True
            seen[num] = i
            i += 1
        return False
        