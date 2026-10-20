# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Iterative BFS
        q = deque([root])
        
        while q:
            r = q.popleft()

            if not r:
                continue

            if self.isSameTree(r, subRoot):
                return True
          
            q.append(r.left)
            q.append(r.right)

        return False

    
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        q.append([root, subRoot])

        while q:
            r, sr = q.popleft()

            if not r and not sr:
                continue
            elif not r or not sr:
                return False

            if r.val != sr.val:
                return False
            
            q.append([r.left, sr.left])
            q.append([r.right, sr.right])

        return True        

        # Time: O(m * n)
        # Space: O(m + n)