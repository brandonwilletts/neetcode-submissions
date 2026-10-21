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
        self.preorder(root, output, k)
        return output[k - 1]

    def preorder(self, root: Optional[TreeNode], output: list, k: int) -> None:
        if not root:
            return
        
        if len(output) < k:
            self.preorder(root.left, output, k)
            output.append(root.val)
            self.preorder(root.right, output, k)

        # Time: O(n)
        # Space: O(n)