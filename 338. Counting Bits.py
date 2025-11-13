'''https://leetcode.com/problems/counting-bits/description/'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            binary = bin(i)[2:]       
            count_ones = binary.count("1")
            result.append(count_ones)

        return result
