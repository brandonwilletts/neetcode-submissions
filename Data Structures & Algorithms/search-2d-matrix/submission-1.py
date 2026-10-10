class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f_row, l_row = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        row = 0

        # Binary search to find row
        while f_row <= l_row:
            mid = (f_row + l_row) // 2

            if target >= matrix[mid][l] and target <= matrix[mid][r]:
                row = mid
                break
            elif target < matrix[mid][l]:
                l_row = mid - 1
            else:
                f_row = mid + 1

        # Binary search within row to find target
        while l <= r:
            mid = (l + r) // 2

            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False

        # Time: O(log(m * n))
        # Space: O(1)