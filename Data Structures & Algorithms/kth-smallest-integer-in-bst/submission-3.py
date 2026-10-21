# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Recursive DFS
        output = []
        self.inorder(root, output, k)
        return output[-1]

    def inorder(self, root: Optional[TreeNode], output: list, k: int) -> None:
        if not root:
            return

        self.inorder(root.left, output, k)

        if len(output) < k:
            output.append(root.val)
            self.inorder(root.right, output, k)

        # Time: O(n)
        # Space: O(n)