class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        highest_left = [0] * len(height)
        highest_right = [0] * len(height)

        # Find highest bar to the left of each bar
        highest = 0
        for i in range(len(height)):
            highest = max(highest, height[i])
            highest_left[i] = highest
            
        # Find highest bar to the right of each bar
        highest = 0
        for i in range(len(height) - 1, -1, -1):
            highest = max(highest, height[i])
            highest_right[i] = highest

        # Calculate trapped water
        for i in range(len(height)):
            water += (min(highest_left[i], highest_right[i]) - height[i])

        return water