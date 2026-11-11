class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        output = []
        atl, pac = set(), set()
        
        q = deque()

        def bfs(r: int, c: int, height: int, ocean: set):
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                height <= heights[r][c] and
                (r, c) not in ocean
            ):
                ocean.add((r, c))
                q.append((r, c))

        # Pacific
        for r in range(ROWS):
            pac.add((r, 0))
            q.append((r, 0))

        for c in range(COLS):
            pac.add((0, c))
            q.append((0, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                bfs(r + 1, c, heights[r][c], pac)
                bfs(r - 1, c, heights[r][c], pac)
                bfs(r, c + 1, heights[r][c], pac)
                bfs(r, c - 1, heights[r][c], pac)
        
        # Atlantic
        for r in range(ROWS):
            atl.add((r, COLS - 1))
            q.append((r, COLS - 1))

        for c in range(COLS):
            atl.add((ROWS - 1, c))
            q.append((ROWS - 1, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                bfs(r + 1, c, heights[r][c], atl)
                bfs(r - 1, c, heights[r][c], atl)
                bfs(r, c + 1, heights[r][c], atl)
                bfs(r, c - 1, heights[r][c], atl)

        for coords in pac:
            if coords in atl:
                output.append(list(coords))

        return output

        # Time: 
        # Space: 
