'''https://leetcode.com/problems/find-the-distinct-difference-array/'''

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [0] * n, [0] * n
        seen_prefix, seen_suffix = set(), set()

        for i in range(n):
            seen_prefix.add(nums[i])
            prefix[i] = len(seen_prefix)

        for i in range(n - 1, -1, -1):
            seen_suffix.add(nums[i])
            suffix[i] = len(seen_suffix)

        ans = []
        for i in range(n):
            right = suffix[i + 1] if i + 1 < n else 0
            ans.append(prefix[i] - right)
        return ans
