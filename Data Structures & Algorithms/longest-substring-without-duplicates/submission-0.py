class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0
        char_set = set()

        while r < len(s):
            if s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            else:
                char_set.add(s[r])
                longest = max(longest, len(char_set))
                r += 1

        return longest


            