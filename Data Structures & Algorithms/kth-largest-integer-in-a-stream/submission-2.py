class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(nums)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
    
    def add(self, val: int) -> int:
        heapq.heappushpop(self.minHeap, val) \
            if len(self.minHeap) >= self.k \
            else heapq.heappush(self.minHeap, val)
        return self.minHeap[0]

    # Time: O(n log(n)) - heapify(), heappop(), heappush()
    # Space: O(n)
    