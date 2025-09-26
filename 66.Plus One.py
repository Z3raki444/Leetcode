'''https://leetcode.com/problems/plus-one/description/'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = len(digits) - 1
        
        # multiply each digit with correct power of 10
        for i in range(len(digits)):
            digits[i] = digits[i] * (10 ** num)
            num -= 1

        total = sum(digits) + 1   # add 1
        return [int(d) for d in str(total)]