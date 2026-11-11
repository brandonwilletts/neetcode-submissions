class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if (
                not(0 <= r < ROWS) or
                not(0 <= c < COLS) or
                board[r][c] != "O"
            ):
                return
            
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Find unsurrounded regions and change to "T"
        for r in range(ROWS):
            for c in range(COLS):
                if (
                    board[r][c] == "O" and (
                        r in [0, ROWS - 1] or
                        c in [0, COLS - 1]
                    )
                ):
                    dfs(r, c)

        # Change O --> X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Change T --> O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        # Time: O(n)
        # Space: O(n)
