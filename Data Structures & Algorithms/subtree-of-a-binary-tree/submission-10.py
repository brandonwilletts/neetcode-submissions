# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Recursive DFS
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        left_subtree = self.isSubtree(root.left, subRoot)
        right_subtree = self.isSubtree(root.right, subRoot)

        return left_subtree or right_subtree


    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False

        left_subtree = self.isSameTree(root.left, subRoot.left)
        right_subtree = self.isSameTree(root.right, subRoot.right)

        if root.val == subRoot.val:
            return left_subtree and right_subtree
        
        return False

        # Time: O(m * n)
        # Space: O(m + n) - call stack