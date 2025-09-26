'''https://leetcode.com/problems/add-binary/description/'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)   # convert binary string to integer
        num2 = int(b, 2)

        total = num1 + num2
        binary_str = bin(total)[2:]   # convert back to binary string (remove "0b")

        return binary_str


