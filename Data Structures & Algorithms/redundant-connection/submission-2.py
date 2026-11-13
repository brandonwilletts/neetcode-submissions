class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        print(parent)
        rank = [1] * (len(edges) + 1)

        def find(node: int) -> int:
            curr = node

            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]

            return curr
        
        def merge(node1: int, node2: int) -> bool:
            root1, root2 = find(node1), find(node2)

            if root1 == root2:
                return False

            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]

            return True

        for a, b in edges:
            if not merge(a, b):
                return [a, b]

        # Time: O(E)
        # Space: O(V)