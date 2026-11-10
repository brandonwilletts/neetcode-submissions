class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterative DFS
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        stack = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    stack.append([r, c])
                    while stack:
                        row, col = stack.pop()
                        if (
                            0 <= row < ROWS and
                            0 <= col < COLS and
                            grid[row][col] == "1"
                        ):
                            grid[row][col] = "0"
                            stack.append([row + 1, col])
                            stack.append([row - 1, col])
                            stack.append([row, col + 1])
                            stack.append([row, col - 1])

                    islands += 1

        return islands

        # Time: O(n)
        # Space: O(n)
