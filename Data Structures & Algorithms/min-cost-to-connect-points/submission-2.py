class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        output = 0
        visited = set()

        minHeap = [[0, 0]]

        while minHeap:
            dist_i, i = heapq.heappop(minHeap)
            
            if i in visited:
                continue

            output += dist_i
            visited.add(i)

            xi, yi = points[i]

            for j in range(len(points)):
                if j != i and j not in visited:
                    xj, yj = points[j]   
                    heapq.heappush(
                        minHeap, 
                        [abs(xi - xj) + abs(yi - yj), j]
                    )
        
        return output

        # Time: 
        # Space: 
