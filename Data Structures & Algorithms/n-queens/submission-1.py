class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        queens = []

        def dfs(row: int) -> None:
            if row == n:
                output.append(self.buildBoard(queens, n))
                
            for col in range(n):
                if self.isValid(queens, (row, col)):
                    queens.append((row, col))
                    dfs(row + 1)
                    queens.pop()

        dfs(0)
        return output

    def isValid(self, queens: list[tuple[int, int]], new: tuple[int, int]) -> bool:
        new_r, new_c = new

        for queen in queens:
            r, c = queen

            # Check rows, cols
            if new_r == r or new_c == c:
                return False

            # Check diagonals
            if new_c == (c + (new_r - r)) or new_c == (c - (new_r - r)):
                return False

        return True

    def buildBoard(self, queens: list[tuple[int, int]], n: int):
        board = [["." for _ in range(n)] for _ in range(n)]
        
        for queen in queens:
            r, c = queen
            board[r][c] = "Q"
        
        return ["".join(row) for row in board]

        # Time: O(n!)
        # Space: O(n^2)
