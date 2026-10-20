# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive DFS

        if not p and not q:
            return True
        elif not p or not q:
            return False

        left_subtree = self.isSameTree(p.left, q.left)
        right_subtree = self.isSameTree(p.right, q.right)

        if p.val == q.val:
            return left_subtree and right_subtree

        return False

        # Time: O(n)
        # Space: O(1)