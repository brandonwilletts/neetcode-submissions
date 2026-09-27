class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        
        for i in range(len(s)):
            freq_s[s[i]] += 1
            freq_t[t[i]] += 1

        return freq_s == freq_t
        
