class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num: int) -> None:
        if not self.minHeap or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
            while (len(self.minHeap) - len(self.maxHeap)) > 1:
                heapq.heappush_max(self.maxHeap, heapq.heappop(self.minHeap))
        else:
            heapq.heappush_max(self.maxHeap, num)
            while (len(self.maxHeap) - len(self.minHeap)) > 1:
                heapq.heappush(self.minHeap, heapq.heappop_max(self.maxHeap))

    def findMedian(self) -> float:
        # Odd length
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            return self.maxHeap[0]
        
        # Even length
        else:
            return (self.minHeap[0] + self.maxHeap[0]) / 2
