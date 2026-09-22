class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = {}, {}, {}

        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]

                if not value.isdigit():
                    continue

                # Check row
                if value in rows.setdefault(r, set()):
                    return False
                else:
                    rows[r].add(value)

                # Check column
                if value in cols.setdefault(c, set()):
                    return False
                else:
                    cols[c].add(value)

                # Check box
                if value in boxes.setdefault((r//3, c//3), set()):
                    return False
                else:
                    boxes[(r//3, c//3)].add(value) 

        return True

