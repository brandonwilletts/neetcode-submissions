# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -math.inf

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            # Set to 0 if negative
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # Find max value: L + Root + R 
            self.max_sum = max(self.max_sum, left_max + root.val + right_max)

            # If negative, it will be set to 0 at the next level
            return max(left_max, right_max) + root.val
            
        dfs(root)
        return self.max_sum

        # Time: O(n)
        # Space: O(n) - call stack
        