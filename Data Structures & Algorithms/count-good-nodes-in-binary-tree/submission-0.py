# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Recursive DFS
        return self.countGoodNodes(root, root.val, 0)

    def countGoodNodes(self, root: Optional[TreeNode], highest: int, count: int) -> int:
        if not root:
            return count

        left_count = self.countGoodNodes(root.left, max(highest, root.val), count)
        right_count = self.countGoodNodes(root.right, max(highest, root.val), count)

        if root.val < highest:
            return left_count + right_count
        
        return left_count + right_count + 1

        
        

        

        