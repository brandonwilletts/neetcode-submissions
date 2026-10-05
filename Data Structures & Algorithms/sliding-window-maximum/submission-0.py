class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums

        output, heap = [], []
        freq = {}

        l = 0

        for r in range(len(nums)):
            heapq.heappush(heap, -nums[r])
            freq[nums[r]] = freq.get(nums[r], 0) + 1
                
            if (r + 1 - l) > k:
                freq[nums[l]] -= 1
                l += 1
            
            if (r + 1 - l) == k:
                while (heap):
                    max_num = -heap[0]
                    if freq[max_num] > 0:
                        output.append(max_num)
                        break
                    else:
                        heapq.heappop(heap)

        return output    

