# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [-math.inf]

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_path = dfs(root.left)
            right_path = dfs(root.right)
            total = 0
            
            # Find max value: L + Root + R 
            total = max(left_path, 0) + root.val + max(right_path, 0)
            max_sum[0] = max(max_sum[0], total)

            # Find max value: L or R + Root (or 0)
            max_subtree = max(left_path, right_path)
            max_subtree = max(max_subtree, 0)

            return max(max_subtree + root.val, 0)
            
        dfs(root)
        return max_sum[0]

        # Time: O(n)
        # Space: O(n) - call stack
        