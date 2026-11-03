class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def dfs(row: int, col: int, i: int):
            if i == len(word):
                return True

            if not(0 <= row < ROWS) or not(0 <= col < COLS):
                return False
            
            if board[row][col] == word[i] and (row, col) not in visited:
                visited.add((row, col))
                
                if not (
                    dfs(row + 1, col, i + 1) or
                    dfs(row - 1, col, i + 1) or
                    dfs(row, col + 1, i + 1) or
                    dfs(row, col - 1, i + 1)
                ):
                    visited.remove((row, col))

                else:
                    return True

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

        # Time: O(n * 4^n)
        # Space: O(n) - Call stack
