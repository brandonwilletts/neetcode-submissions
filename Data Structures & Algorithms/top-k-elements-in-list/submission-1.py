class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        freq = defaultdict(int)

        for num in nums:
            freq[num] = freq[num] + 1

        # Reverse look-up table
        freq_sorted = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            freq_sorted[count].append(num)
        
        # Bucket sort
        output = []

        for i in range(len(freq_sorted) - 1, -1, -1):
            for num in freq_sorted[i]:
                output.append(num)
                if len(output) == k:
                    return output