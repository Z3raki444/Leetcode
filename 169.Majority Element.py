'''https://leetcode.com/problems/majority-element/description/'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        n = len(nums)
        for x in nums:
            freq[x] += 1
            if freq[x] > n // 2:
                return x