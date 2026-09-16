class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1

        while (left < right):
            # n-1 rotations for each layer
            for i in range(right - left):
                top, bottom = left, right

                # Save topLeft to temporary variable for each rotation
                topLeft = matrix[top][left + i]

                # Rotate bottomLeft to topLeft
                matrix[top][left + i] = matrix[bottom - i][left]

                # Rotate bottomRight to bottomLeft
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Rotate topRight to bottomLeft
                matrix[bottom][right - i] = matrix[top + i][right]

                # Rotate topLeft to topRight
                matrix[top + i][right] = topLeft
            
            # Increment pointers
            left += 1
            right -= 1