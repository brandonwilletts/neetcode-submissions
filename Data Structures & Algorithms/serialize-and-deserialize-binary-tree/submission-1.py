# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Recursive DFS
        def dfs(node: Optional[TreeNode]) -> str:
            if not node: return "n"
            return str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)
        
        return dfs(root)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        input_data = data.split(",")
        vals = iter(input_data)

        print(input_data)

        def dfs():
            curr = next(vals)

            if curr == "n": return None

            node = TreeNode(int(curr))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
        