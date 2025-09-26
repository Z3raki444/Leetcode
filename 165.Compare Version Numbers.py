'''https://leetcode.com/problems/compare-version-numbers/description/'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split(".")
        b = version2.split(".")

        num = max(len(a),len(b))

        for i in range(num):
            x = int(a[i]) if i < len(a) else 0
            y = int(b[i]) if i < len(b) else 0
            if x > y: return 1
            if x < y: return -1
        return 0


        