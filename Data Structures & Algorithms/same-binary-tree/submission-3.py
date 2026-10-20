# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative BFS

        qu = deque()
        qu.append([p, q])

        while qu:
            for _ in range(len(qu)):
                p_root, q_root = qu.popleft()

                if not p_root and not q_root:
                    continue
                elif not p_root or not q_root:
                    return False

                if p_root.val != q_root.val:
                    return False
                
                qu.append([p_root.left, q_root.left])
                qu.append([p_root.right, q_root.right])

        return True

        # Time: O(n)
        # Space: O(n)
        