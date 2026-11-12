class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        output = 0

        nodeMap = {i: [] for i in range(n)}

        for a, b in edges:
            nodeMap[a].append(b)
            nodeMap[b].append(a)

        processed = set()

        def dfs(node: int) -> None:
            if node in processed:
                return

            processed.add(node)

            for neighbor in nodeMap[node]:
                dfs(neighbor)

        for node in nodeMap:
            if node not in processed:
                dfs(node)
                output += 1

        return output

        # Time: O(V + E)
        # Space: O(V + E)
