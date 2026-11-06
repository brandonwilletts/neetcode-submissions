class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []

        minHeap = [[math.sqrt(p[0]**2 + p[1]**2), p] for p in points]
        heapq.heapify(minHeap)

        for _ in range(k):
            output.append(heapq.heappop(minHeap)[1])

        return output

        # Time: O(n log(n)) - heapify(), heappop()
        # Space: O(n)
