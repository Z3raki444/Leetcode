'''https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/description/'''

class Solution:
    def maxOperations(self, nums: List[int]) -> int:

        score = nums[0] + nums[1]
        operations = 1 
        

        for i in range(2, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] == score:
                operations += 1
            else:
                break
        
        return operations
