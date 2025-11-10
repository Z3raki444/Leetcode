'''https://leetcode.com/problems/number-complement/description/'''

class Solution:
    def findComplement(self, num: int) -> int:
        
        binary_string = bin(num)[2:]
        
        complemented_string = ''
        for bit in binary_string:
            if bit == '1':
                complemented_string += '0'
            else: 
                complemented_string += '1'
    
        result = int(complemented_string, 2)
        
        return result