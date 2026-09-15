class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if (stone1 > stone2):
                heapq.heappush_max(stones, stone1 - stone2)

        # Append 0 in case array is empty
        stones.append(0)
        return stones[0]