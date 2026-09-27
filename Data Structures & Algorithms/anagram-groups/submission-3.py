class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        freq = defaultdict(list)
        
        for string in strs:
            # Build frequency array
            freq_arr = [0] * 26

            for ch in string:
                freq_arr[ord(ch) - ord("a")] += 1

            # Add to frequency hash map
            freq[tuple(freq_arr)].append(string)

        return list(freq.values())
