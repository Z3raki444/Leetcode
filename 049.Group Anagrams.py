'''https://leetcode.com/problems/group-anagrams/description/'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))   # sort characters
            groups[key].append(word)
        
        return list(groups.values())
