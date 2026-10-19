# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS

        self.diameter = 0
        
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_h = dfs(root.left)
            right_h = dfs(root.right)

            self.diameter = max(self.diameter, left_h + right_h)

            return max(left_h, right_h) + 1

        dfs(root)
        return self.diameter

    # Time: O(n)
    # Space: O(n)