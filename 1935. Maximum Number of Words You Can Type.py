''' https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/'''

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        letters = set(brokenLetters)
        output = 0
        result = text.split(" ")

        # check each word
        for word in result:
            if all(c not in letters for c in word):  # no broken letters inside word
                output += 1

        return output
