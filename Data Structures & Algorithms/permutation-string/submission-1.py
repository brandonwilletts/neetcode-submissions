class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        if n1 > n2:
            return False
        
        s1_freq, s2_freq = [0] * 26, [0] * 26

        # Initialize frequency arrays
        for i in range(n1):
            s1_freq[ord(s1[i]) - ord("a")] += 1
            s2_freq[ord(s2[i]) - ord("a")] += 1

        if s1_freq == s2_freq:
                return True
        
        # Traverse s2
        for r in range(n1, n2):
            l = r - n1

            # Expand window
            s2_freq[ord(s2[r]) - ord("a")] += 1

            # Shrink window
            s2_freq[ord(s2[l]) - ord("a")] -= 1

            # Check if s2 contains permutation substring of s1
            if s1_freq == s2_freq:
                return True

        return False