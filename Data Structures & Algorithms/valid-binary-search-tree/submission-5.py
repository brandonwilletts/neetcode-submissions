# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Iterative DFS
        stack = [[root, -math.inf, math.inf]]

        while stack:
            node, low_bound, high_bound = stack.pop()
            
            if not(low_bound < node.val < high_bound):
                return False
            
            if node.left:
                stack.append([node.left, low_bound, node.val])
            if node.right:
                stack.append([node.right, node.val, high_bound])
            
        return True
        
        # Time: O(n)
        # Space: O(n)
        