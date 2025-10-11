'''https://leetcode.com/problems/valid-word/description/'''

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = [
            'b','c','d','f','g','h','j','k','l','m',
            'n','p','q','r','s','t','v','w','x','y','z'
        ]
        digits = ['0','1','2','3','4','5','6','7','8','9']

        word = word.lower()

        vo = 0
        con = 0
        digit = 0

        if len(word) >= 3:
            for ch in word:
                if ch in vowels:
                    vo += 1
                elif ch in consonants:
                    con += 1
                elif ch in digits:
                    digit += 1
                else:
                    return False  

            if vo >= 1 and con >= 1:
                return True
        return False