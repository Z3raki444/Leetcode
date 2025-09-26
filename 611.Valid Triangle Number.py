'''https://leetcode.com/problems/valid-triangle-number/description/'''

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # ignore non-positive sides (can't form triangles)
        nums = [x for x in nums if x > 0]
        nums.sort()  # so we only need to check a + b > c
        n = len(nums)
        count = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    # since nums[i] <= nums[j] <= nums[k], just check this:
                    if nums[i] + nums[j] > nums[k]:
                        count += 1
        return count