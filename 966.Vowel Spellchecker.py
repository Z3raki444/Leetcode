''' https://leetcode.com/problems/vowel-spellchecker/description/'''

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")
        
        def devowel(s: str) -> str:
            # Lowercase + replace vowels with '*'
            s = s.lower()
            return ''.join('*' if c in vowels else c for c in s)
        
        # 1) Exact match set
        exact = set(wordlist)
        
        # 2) Case-insensitive: first occurrence wins
        first_lower = {}
        # 3) Vowel-error map (on lowercase): first occurrence wins
        first_devowel = {}
        
        for w in wordlist:
            lw = w.lower()
            dv = devowel(w)
            if lw not in first_lower:
                first_lower[lw] = w
            if dv not in first_devowel:
                first_devowel[dv] = w
        
        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
                continue
            
            lq = q.lower()
            if lq in first_lower:
                ans.append(first_lower[lq])
                continue
            
            dq = devowel(q)
            if dq in first_devowel:
                ans.append(first_devowel[dq])
                continue
            
            ans.append("")
        
        return ans
