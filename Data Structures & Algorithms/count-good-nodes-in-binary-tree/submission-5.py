# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Iterative DFS
        stack = [[root, root.val]]
        count = 0

        while stack:
            node, highest = stack.pop()

            if node.val >= highest:
                count += 1
                highest = node.val

            if node.left:
                stack.append([node.left, highest])
            if node.right:
                stack.append([node.right, highest])

        return count

        # Time: O(n)
        # Space: O(n)