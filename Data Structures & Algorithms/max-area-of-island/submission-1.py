class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Recursive DFS
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def dfs(r: int, c: int) -> int:
            if (
                not(0 <= r < ROWS) or
                not(0 <= c < COLS) or
                grid[r][c] != 1
            ):
                return 0

            grid[r][c] = 0

            return (
                dfs(r + 1, c) + 
                dfs(r - 1, c) +
                dfs(r, c + 1) + 
                dfs(r, c - 1) + 1
            )

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))

        return area

        # Time: O(n)
        # Space: O(n) - Call stack
