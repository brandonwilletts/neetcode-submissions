# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Iterative BFS

        if not root:
            return True

        q = deque([root])
        heights = {}

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

                    heights[node] = max(left_h, right_h) + 1

                    if abs(left_h - right_h) > 1:
                        return False

        return True

    # Time: O(n)
    # Space: O(n)
