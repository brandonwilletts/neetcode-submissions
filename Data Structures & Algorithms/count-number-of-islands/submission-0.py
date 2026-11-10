class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            if (
                not(0 <= r < ROWS) or 
                not(0 <= c < COLS) or
                grid[r][c] == "0"
            ):
                return
            
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands

        # Time: O(n)
        # Space: O(n) - Call stack
        