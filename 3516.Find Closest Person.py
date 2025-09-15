'''https://leetcode.com/problems/find-closest-person/description/'''

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz = abs(z-x)
        yz = abs(y-z)
        
        if xz > yz :
            return 2
        elif yz > xz :
            return 1
        else:
            return 0