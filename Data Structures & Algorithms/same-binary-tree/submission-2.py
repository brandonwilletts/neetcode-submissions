# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative DFS

        stack = [[p, q]]

        while stack:
            p_root, q_root = stack.pop()

            if not p_root and not q_root:
                continue
            elif not p_root or not q_root:
                return False
            
            stack.append([p_root.left, q_root.left])
            stack.append([p_root.right, q_root.right])

            if p_root.val != q_root.val:
                return False
        
        return True

        # Time: O(n)
        # Space: O(n)
            