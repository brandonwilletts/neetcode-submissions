class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Iterative DFS
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        stack = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    stack.append([r, c])
                    curr_area = 0
                    while stack:
                        row, col = stack.pop()
                        if (
                            0 <= row < ROWS and
                            0 <= col < COLS and
                            grid[row][col] == 1
                        ):
                            grid[row][col] = 0
                            curr_area += 1
                            stack.append([row + 1, col])
                            stack.append([row - 1, col])
                            stack.append([row, col + 1])
                            stack.append([row, col - 1])

                    area = max(area, curr_area)

        return area

        # Time: O(n)
        # Space: O(n)