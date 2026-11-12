class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        preMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visited = set()
        processed = set()

        def dfs(course: int) -> bool:
            if course in visited:
                return False

            if course in processed:
                return True
            
            visited.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            processed.add(course)
            output.append(course)

            return True

        for course in preMap:
            if not dfs(course):
                return []
        
        return output

        # Time: O(V + E)
        # Space: O(V + E)
