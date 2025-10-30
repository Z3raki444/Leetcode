'''https://leetcode.com/problems/smallest-number-with-all-set-bits/description/'''

class Solution:
    def smallestNumber(self, n: int) -> int:
       
        binary = bin(n)[2:]
        
      
        if len(set(binary)) == 1 and '1' in set(binary):
            return n
            
        i = 1
        while True:
            m = n + i
            binary_m = bin(m)[2:]
           
            if len(set(binary_m)) == 1 and '1' in set(binary_m):
                return m
            
            i += 1