'''https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/'''

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if b == 2 * (a + c):
                ans += 1
        return ans
