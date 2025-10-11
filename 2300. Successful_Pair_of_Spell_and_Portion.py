'''https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/'''

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        lst = []
        for i in spells:
            count = 0
            for j in potions:
                if i*j >= success:
                    count += 1
            lst.append(count)

        return lst