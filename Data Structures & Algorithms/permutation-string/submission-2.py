class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_freq, s2_freq = [0] * 26, [0] * 26
        l = 0

        # Create s1 frequency array
        for ch in s1:
            s1_freq[ord(ch) - ord("a")] += 1
        
        # Traverse s2
        for r in range(len(s2)):
            # Expand window
            s2_freq[ord(s2[r]) - ord("a")] += 1

            # Shrink window (make valid)
            while (r - l + 1) > len(s1):
                s2_freq[ord(s2[l]) - ord("a")] -= 1
                l += 1

            # Check if s2 contains permutation substring of s1
            if s1_freq == s2_freq:
                return True

        return False