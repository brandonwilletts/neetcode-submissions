class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        output = []
        atl, pac = set(), set()
        
        

        def add(r: int, c: int, height: int, ocean: set, q: deque) -> None:
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                height <= heights[r][c] and
                (r, c) not in ocean
            ):
                ocean.add((r, c))
                q.append((r, c))

        def bfs(ocean: set) -> None:
            q = deque(ocean)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    add(r + 1, c, heights[r][c], ocean, q)
                    add(r - 1, c, heights[r][c], ocean, q)
                    add(r, c + 1, heights[r][c], ocean, q)
                    add(r, c - 1, heights[r][c], ocean, q)     

        for r in range(ROWS):
            pac.add((r, 0))
            atl.add((r, COLS - 1))

        for c in range(COLS):
            pac.add((0, c))
            atl.add((ROWS - 1, c))

        bfs(pac)
        bfs(atl)

        for coords in pac:
            if coords in atl:
                output.append(list(coords))

        return output

        # Time: O(n)
        # Space: O(n)
