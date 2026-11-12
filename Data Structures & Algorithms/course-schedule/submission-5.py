class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}
        checked = set()

        for a, b in prerequisites:
            if a not in prereqs:
                prereqs[a] = []
            prereqs[a].append(b)

        def dfs(curr: int, visited: set) -> bool:
            if curr not in prereqs or curr in checked:
                return True

            if curr in visited:
                return False

            visited.add(curr)
            
            for b in prereqs[curr]:
                if not dfs(b, visited):
                    return False
                    
            checked.add(curr)
            return True

        for a in prereqs:
            if a not in checked and not dfs(a, set()):
                return False

        return True

        # Time: O(V + E)
        # Space: O(V + E)
