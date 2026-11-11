class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        
        q = deque()

        # Add rotten fruit to q and count fresh fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        if fresh == 0:
            return 0

        fresh += len(q)

        def traverse(r: int, c: int) -> None:
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                grid[r][c] == 1
            ):
                grid[r][c] = 2
                q.append([r, c])

        # BFS
        while q:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                fresh -= 1

                traverse(r + 1, c)
                traverse(r - 1, c)
                traverse(r, c + 1)
                traverse(r, c - 1)

        if fresh > 0:
            return -1
        
        return time - 1

        # Time: O(n)
        # Space: O(1)