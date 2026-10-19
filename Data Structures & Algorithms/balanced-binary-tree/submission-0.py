# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Recursive DFS
        
        self.heights = {}

        def dfs(root: Optional[TreeNode]) -> bool:
            if not root:
                return True

            if dfs(root.left) and dfs(root.right):
                left_h = self.heights.get(root.left, 0)
                right_h = self.heights.get(root.right, 0)

                self.heights[root] = max(left_h, right_h) + 1

                return abs(left_h - right_h) <= 1

            return False
        
        return dfs(root)

    # Time: O(n)
    # Space: O(n)
