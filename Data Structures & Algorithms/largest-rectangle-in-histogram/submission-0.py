class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        n = len(heights)
        stack = [] # [index, height]

        for i, h in enumerate(heights):
            # Start of rectangle formed by curr
            start = i

            while stack and h < stack[-1][1]:
                # Process prev since it cannot extend right
                prev_start, prev_h = stack.pop()
                prev_area = prev_h * (i - prev_start)
                largest = max(largest, prev_area)

                # Update start of rectangle formed by curr
                start = prev_start
            
            stack.append([start, h])
        
        # Process remaining items in stack
        while stack:
            prev_start, prev_h = stack.pop()
            prev_area = prev_h * (n - prev_start)
            largest = max(largest, prev_area)

        return largest
     
    # Time: O(n)
    # Space: O(n)