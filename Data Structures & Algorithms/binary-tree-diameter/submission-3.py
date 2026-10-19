# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Iterative BFS

        if not root:
            return 0

        q = deque([root])
        heights = {}
        diameter = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                
                if node.left and node.left not in heights:
                    q.append(node.left)
                    q.append(node)

                elif node.right and node.right not in heights:
                    q.append(node.right)
                    q.append(node)

                else:
                    left_h = heights.get(node.left, 0)
                    right_h = heights.get(node.right, 0)

                    diameter = max(diameter, left_h + right_h)
                    heights[node] = max(left_h, right_h) + 1

        return diameter

        # Time: O(n)
        # Space: O(n)