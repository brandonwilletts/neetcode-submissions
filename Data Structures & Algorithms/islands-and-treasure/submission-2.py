class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dist = 1

        q = deque()

        def traverse(r: int, c: int, dist: int) -> None:
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                grid[r][c] > dist
            ):
                grid[r][c] = dist
                q.append([r, c])
            
        # Add 0s to q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])

        # BFS
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                traverse(r + 1, c, dist)
                traverse(r - 1, c, dist)
                traverse(r , c + 1, dist)
                traverse(r , c - 1, dist)
            dist += 1
        
        # Time: O(n)
        # Space: O(1)
