'''https://leetcode.com/problems/uncommon-words-from-two-sentences/description/'''

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()

        count = Counter(words)
        return [word for word, freq in count.items() if freq == 1]