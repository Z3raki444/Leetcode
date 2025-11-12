'''https://leetcode.com/problems/count-pairs-of-similar-strings/description/'''

class Solution:
    def similarPairs(self, words: List[str]) -> int:

        uniq_sets = [set(w) for w in words]

        count = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if uniq_sets[i] == uniq_sets[j]:
                    count += 1

        return count
