class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        row = 0

        # Binary search to find row
        first, last = 0, ROWS - 1

        while first <= last:
            mid = (first + last) // 2

            if target < matrix[mid][0]:
                last = mid - 1
            elif target > matrix[mid][COLS - 1]:
                first = mid + 1
            else:
                row = mid
                break

        # Target not found in any row
        if not first <= last:
            return False
    
        # Binary search within row to find target
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2

            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False

        # Time: O(log(m + n))
        # Space: O(1)