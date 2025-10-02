'''https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/'''

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        # dp[i][j] = minimum score triangulation for sub-polygon [i...j]
        dp = [[0] * n for _ in range(n)]
        
        # We need at least 3 vertices to form a triangle
        for length in range(3, n + 1):          # sub-polygon size
            for i in range(n - length + 1):     # starting index
                j = i + length - 1              # ending index
                dp[i][j] = float('inf')
                
                # Try all possible "k" to form triangle (i, k, j)
                for k in range(i + 1, j):
                    score = values[i] * values[j] * values[k]
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + score)
        
        return dp[0][n - 1]