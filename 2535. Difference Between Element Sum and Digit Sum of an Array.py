'''https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/'''

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        Elemental_sum = sum(nums)

        Digital_sum = []
        for n in nums:
            if n > 9:
                Digital_sum.extend([int(d) for d in str(n)])
            else:
                Digital_sum.append(n)

        result = abs(sum(Digital_sum) - Elemental_sum)
        return result