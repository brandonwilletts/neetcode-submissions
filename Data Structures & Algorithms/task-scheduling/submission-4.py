class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        count = Counter(tasks)
        
        maxHeap = [count for count in count.values()]
        heapq.heapify_max(maxHeap)

        q = deque()

        while maxHeap or q:
            time += 1

            # Process task, decrement count, append to q with "time to next"
            if maxHeap:
                count = heapq.heappop_max(maxHeap) - 1
                if count:
                    q.append([count, time + n])

            # If item in q eligible, add to heap
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])

        return time

        # Time: O(n)
        # Space: O(n)
