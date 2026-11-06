class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []

        minHeap = [[self.calcDist(point), i] for i, point in enumerate(points)]
        heapq.heapify(minHeap)

        for _ in range(k):
            output.append(points[heapq.heappop(minHeap)[1]])

        return output

    def calcDist(self, point: List[int]) -> float:
        x, y = point
        return math.sqrt(x**2 + y**2)

        # Time: O(n log(n)) - heapify(), heappop()
        # Space: O(n)
