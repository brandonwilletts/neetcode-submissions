class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)

            if x < y:
                heapq.heappush_max(stones, y - x)
        
        if not stones:
            return 0

        return stones[0]

        # Time: O(n log(n)) - heapify is O(n), heappush / pop is O(log(n))
        # Space: O(1)
