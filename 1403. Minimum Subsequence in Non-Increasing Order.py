'''https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/'''

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True) 
        result = []

        total_sum = sum(nums)

        for num in nums:
            result.append(num)
            if sum(result) > total_sum - sum(result):
                break

        return result
