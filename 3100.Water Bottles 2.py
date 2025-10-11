'''https://leetcode.com/problems/water-bottles-ii/description/'''

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empties = numBottles

        while empties >= numExchange:
            empties -= numExchange
            drank = drank + 1
            empties = empties + 1
            numExchange = numExchange + 1
        return drank

        