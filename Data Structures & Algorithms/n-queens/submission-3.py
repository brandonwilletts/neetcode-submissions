class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []

        board = [["."] * n for i in range(n)]
        cols, posDiag, negDiag = set(), set(), set()

        def backtrack(r: int) -> None:
            if r == n:
                output.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)
                
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        
        return output
            
        # Time: O(n * n!)
        # Space: O(n^2) - Temporary board
