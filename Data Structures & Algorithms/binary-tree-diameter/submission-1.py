# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS

        if not root:
            return 0

        stack = [root]
        heights = {}
        diameter = 0

        while stack:
            node = stack[-1]

            if node.left and node.left not in heights:
                stack.append(node.left)

            elif node.right and node.right not in heights:
                stack.append(node.right)

            else:
                node = stack.pop()

                left_h = heights.get(node.left, 0)
                right_h = heights.get(node.right, 0)

                diameter = max(diameter, left_h + right_h)
                heights[node] = max(left_h, right_h) + 1            

        return diameter