class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return matrix
        
        rows, cols = len(matrix), len(matrix[0])
        first_row = matrix[0][0]

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # Mark column
                    matrix[0][c] = 0
                    # Mark row
                    if r == 0:
                        first_row = 0
                    else:
                        matrix[r][0] = 0
        
        # Change column values except first column
        for c in range(1, cols):
            if matrix[0][c] == 0:
                # Zero out column
                for r in range(rows):
                    matrix[r][c] = 0
        
        # Change row values except first row
        for r in range(1, rows):
            if matrix[r][0] == 0:
                # Zero out row
                for c in range (cols):
                    matrix[r][c] = 0

        # Change first column
        if matrix[0][0] == 0:
            # Zero out column
            for r in range(rows):
                matrix[r][0] = 0

        # Change first row
        if first_row == 0:
            # Zero out row
            for c in range (cols):
                matrix[0][c] = 0


