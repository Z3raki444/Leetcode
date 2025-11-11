'''https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:


        product = 1
        for digit in str(n):
            product *= int(digit)

        total = 0
        for digit in str(n):
            total += int(digit)

        return (product - total)

        



        