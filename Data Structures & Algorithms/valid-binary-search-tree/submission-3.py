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

    def dfs_isValidBST(self, root: Optional[TreeNode], left_bound: float, right_bound: float) -> bool:
        if not root:
            return True

        if not(root.val > left_bound and root.val < right_bound):
            return False      
        
        return (
            self.dfs_isValidBST(root.left, left_bound, root.val) and 
            self.dfs_isValidBST(root.right, root.val, right_bound)
        )

        # Time: O(n)
        # Space: O(n)
