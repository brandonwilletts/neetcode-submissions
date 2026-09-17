class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[tuple[int,...], List[str] ]  = {}

        for word in strs:
            ch_count = [0] * 26

            for ch in word:
                ch_count[ord(ch) - ord('a')] += 1
            
            if tuple(ch_count) in anagrams.keys():
                anagrams[tuple(ch_count)].append(word)
            else:
                anagrams[tuple(ch_count)] = [word]  

        return list(anagrams.values())