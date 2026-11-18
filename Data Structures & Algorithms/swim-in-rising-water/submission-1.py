class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visited = set()
        minHeap = [[grid[0][0], 0, 0]]

        visited.add((0,0))

        while minHeap:
            el, r, c = heapq.heappop(minHeap)
    
            # Reached the end
            if r == N - 1 and c == N - 1:
                return el

            # Add unvisited neighbors to minHeap
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    not(0 <= nr < N) or
                    not(0 <= nc < N) or
                    (nr, nc) in visited
                ):
                    continue

                visited.add((nr, nc))
                heapq.heappush(minHeap, [max(el, grid[nr][nc]), nr, nc])

        # Time: O(n^2 log(n))
        # Space: O(n^2)
