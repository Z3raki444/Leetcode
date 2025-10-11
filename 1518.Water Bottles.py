'''https://leetcode.com/problems/water-bottles/description/'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles       
        empties = numBottles      

        while empties >= numExchange:
            new_bottles = empties // numExchange   
            total += new_bottles                  
            empties = new_bottles + (empties % numExchange)

        return total