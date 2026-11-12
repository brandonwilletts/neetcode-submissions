class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        visited = set()

        for a, b in prerequisites:
            prereqs[a].append(b)

        def dfs(curr: int) -> bool:
            if curr in visited:
                return False

            if not prereqs[curr]:
                return True

            visited.add(curr)
            
            for b in prereqs[curr]:
                if not dfs(b):
                    return False
            
            visited.remove(curr)
            prereqs[curr] = []

            return True

        for a in prereqs:
            if prereqs[a] and not dfs(a):
                return False

        return True

        # Time: O(V + E)
        # Space: O(V + E)
