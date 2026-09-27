class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        water = 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]

        while l < r:
            if max_left <= max_right:
                l += 1
                max_left = max(max_left, height[l])
                water += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                water += max_right - height[r]

        return water