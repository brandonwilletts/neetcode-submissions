class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {i: [] for i in range(n)}

        for edge in edges:
            edgeMap[edge[0]].append(edge[1])
            edgeMap[edge[1]].append(edge[0])

        visited = set()

        def dfs(node: int, prev: int|None) -> bool:
            if node in visited:
                return False

            visited.add(node)

            for neighbor in edgeMap[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True
        
        return dfs(0, None) and len(visited) == n

        # Time: O(V + E)
        # Space: O(V + E)
