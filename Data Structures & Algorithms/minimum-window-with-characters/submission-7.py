class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        output = ""
        freq_t, freq_curr = {}, {}

        # Build char frequencies for t
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1

        have, need = 0, len(freq_t)
        l = 0

        for r in range(len(s)):
            if s[r] in freq_t:
                freq_curr[s[r]] = freq_curr.get(s[r], 0) + 1

                if freq_curr[s[r]] == freq_t[s[r]]:
                    have += 1
            
            # If curr substring contains t, shrink window
            while have == need:

                # Update output if curr substring shorter
                if output == "" or (r + 1 - l) < len(output):
                    output = s[l:r + 1]

                # Shrink window on left side
                if s[l] in freq_t:
                    freq_curr[s[l]] -= 1
                    if freq_curr[s[l]] < freq_t[s[l]]:
                        have -= 1

                l += 1

        return output

        # Time: O(n)
        # Space: O(n)