# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Iterative DFS
        stack = [root]

        while stack:
            r = stack.pop()

            if not r:
                continue

            if self.isSameTree(r, subRoot):
                return True
            
            stack.append(r.left)
            stack.append(r.right)
        
        return False


    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [[root, subRoot]]

        while stack:
            r, sr = stack.pop()

            if not r and not sr:
                continue
            elif not r or not sr:
                return False

            if r.val != sr.val:
                return False
            
            stack.append([r.left, sr.left])
            stack.append([r.right, sr.right])

        return True

        # Time: O(n)
        # Space: O(n)        