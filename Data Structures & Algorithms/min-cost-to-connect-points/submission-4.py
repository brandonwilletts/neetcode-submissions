class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        output = 0
        n = len(points)

        dist = [math.inf] * n
        visited = set()

        edges, node = 0, 0

        while edges < (n - 1):
            visited.add(node)
            xi, yi = points[node][0], points[node][1]

            nextNode = -1

            # For every unvisited point j...
            for j in range(n):
                if j in visited:
                    continue

                # Compute the distance to connect j from the current node
                xj, yj = points[j][0], points[j][1]
                dist[j] = min(dist[j], abs(xi - xj) + abs(yi - yj))

                # Choose nextNode as the unvisited point with the shortest distance
                if nextNode == -1 or dist[j] < dist[nextNode]:
                    nextNode = j

            # Update totals and move node
            output += int(dist[nextNode])
            node = nextNode
            edges += 1

        return output

        # Time: O(n^2)
        # Space: O(n^2)
