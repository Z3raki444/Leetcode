'''https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/'''

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        compressed = [nums[0]]
        for x in nums[1:]:
            if x != compressed[-1]:
                compressed.append(x)
        nums = compressed

        total = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                total += 1
            elif nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                total += 1

        return total