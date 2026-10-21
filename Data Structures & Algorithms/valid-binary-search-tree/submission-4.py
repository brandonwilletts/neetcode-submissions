# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Recursive DFS
        return self.dfs_isValidBST(root, -math.inf, math.inf)

    def dfs_isValidBST(self, root: Optional[TreeNode], low_bound: float, high_bound: float) -> bool:
        if not root:
            return True

        if not(low_bound < root.val < high_bound):
            return False      
        
        return (
            self.dfs_isValidBST(root.left, low_bound, root.val) and 
            self.dfs_isValidBST(root.right, root.val, high_bound)
        )

        # Time: O(n)
        # Space: O(n)
