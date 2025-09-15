'''https://leetcode.com/problems/minimum-number-of-people-to-teach/description/'''

from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        lang_sets = [set(langs) for langs in languages]
        
        
        broken = set()
        for u, v in friendships:
            u -= 1; v -= 1
            if not (lang_sets[u] & lang_sets[v]):
                broken.add(u)
                broken.add(v)
        
        
        if not broken:
            return 0
        
        
        counts = [0] * (n + 1)  
        for person in broken:
            for lang in lang_sets[person]:
                counts[lang] += 1
        

        return len(broken) - max(counts)