# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Recursive DFS
        return self.countGoodNodes(root, root.val)

    def countGoodNodes(self, root: Optional[TreeNode], highest: int) -> int:
        if not root:
            return 0

        highest = max(highest, root.val)

        count = self.countGoodNodes(root.left, highest) +           self.countGoodNodes(root.right, highest)

        if root.val < highest:
            return count
        
        return count + 1

        # Time: O(n)
        # Space: O(n) - call stack        