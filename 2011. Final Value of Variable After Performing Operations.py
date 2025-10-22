'''https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/'''

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        X = 0
        for op in operations:
            if '+' in op:
                X += 1
            else:
                X -= 1
        return X
        