'''https://leetcode.com/problems/clear-digits/description/'''

class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)          
        left, right = 0, 1

        while right < len(s):
            if s[right].isdigit():
                s.pop(right)  
                s.pop(left)   
                left = max(0, left - 1)
                right = left + 1
            else:
                left += 1
                right += 1

        return "".join(s)
