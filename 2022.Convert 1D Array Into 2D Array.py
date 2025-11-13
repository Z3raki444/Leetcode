'''https://leetcode.com/problems/convert-1d-array-into-2d-array/description/'''

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m*n != len(original):
            return []
        
        result = []
        for i in range(m):
            result.append(original[i*n : (i+1)*n])
        return result

