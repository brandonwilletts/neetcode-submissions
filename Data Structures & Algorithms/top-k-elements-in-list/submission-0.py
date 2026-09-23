class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        freq_sorted = [[] for _ in range(len(nums) + 1)]
        output = []

        # Count frequencies
        for num in nums:
            freq[num] += 1
        
        # Create reverse look-up
        for num, count in freq.items():
            freq_sorted[count].append(num)

        # Traverse reverse look-up
        for i in range(len(freq_sorted) -1, -1, -1):
            for num in freq_sorted[i]:
                output.append(num)
                if len(output) == k:
                    return output

        return output