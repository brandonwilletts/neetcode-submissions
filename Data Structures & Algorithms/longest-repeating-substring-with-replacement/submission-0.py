class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, max_freq = 0, 0
        freq = defaultdict(int)
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
            
            # Make valid
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l + 1))

        return longest