class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = {i: [] for i in range(1, n + 1)}

        for u, v, t in times:
            adjMap[u].append([v, t])

        minHeap = [[0, k]]
        visited = set()
        t = 0

        while minHeap:
            t_curr, u_curr = heapq.heappop(minHeap)

            if u_curr in visited:
                continue

            visited.add(u_curr)
            t = max(t, t_curr)

            for v_child, t_child in adjMap[u_curr]:
                if v_child not in visited:
                    heapq.heappush(minHeap, [t_curr + t_child, v_child])

        return t if len(visited) == n else -1

        # Time: O(E log(V))
        # Space: O(V + E)
