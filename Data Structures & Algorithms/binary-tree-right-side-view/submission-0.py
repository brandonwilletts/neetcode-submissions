# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        output = []
        q = deque([root])

        while q:
            len_q = len(q)
            right_node = None

            for i in range(len_q):
                node = q.popleft()

                if node:
                    right_node = node
                    q.append(node.left)
                    q.append(node.right)

            if right_node:
                output.append(right_node.val)
        
        return output

        # Time: O(n)
        # Space: O(n)
