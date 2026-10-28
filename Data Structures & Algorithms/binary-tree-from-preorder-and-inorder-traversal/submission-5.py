# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Look-up table --> val: index
        inorder_indices = {val: i for i, val in enumerate(inorder)}

        # Root index in preorder -> has to be a list (mutable)
        preorder_root_index = [0]

        def recBuildTree(l, r) -> Optional[TreeNode]:
            if l > r:
                return None

            # Create root from preorder
            root_val = preorder[preorder_root_index[0]]
            root = TreeNode(root_val)
            preorder_root_index[0] += 1

            # Get root index in inorder
            root_index = inorder_indices[root_val]

            # Recursive calls with shrinking windows
            root.left = recBuildTree(l, root_index - 1)
            root.right = recBuildTree(root_index + 1, r)

            return root

        return recBuildTree(0, len(preorder) - 1)

        # Time: O(n)
        # Space: O(n)