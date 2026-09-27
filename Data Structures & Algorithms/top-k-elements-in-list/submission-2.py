class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        freq = defaultdict(int)

        # Count frequency of each digit
        for num in nums:
            freq[num] += 1
        
        # Reverse look-up for frequencies (bucket sort)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # Gather results
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output