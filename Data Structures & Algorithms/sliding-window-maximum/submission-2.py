class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = collections.deque()

        l = 0

        for r in range(len(nums)):
            # Pop smaller values from dequeue
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            # Pop values from dq if outside window
            if l > dq[0]:
                dq.popleft()
            
            # Append highest value to output once window size == k
            if (r + 1) >= k:
                output.append(nums[dq[0]])
                l += 1

        return output    
        
        # Time: O(n)
        # Space: O(n)