'''https://leetcode.com/problems/count-square-sum-triples/description/'''

class Solution:
    def countTriples(self, n: int) -> int:
        
        count = 0

        for a in range(1,n+1):
            for b in range(1,n+1):
                c = sqrt(a*a + b*b)
                if int(c) == c and c <= n:
                    count += 1

        return count

    
