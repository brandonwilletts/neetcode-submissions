class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # Mid is in the left sorted portion
            if nums[mid] >= nums[l]:
                # Search right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # Search left
                else: 
                    r = mid - 1

            # Mid is in the right sorted portion
            else:
                # Search left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # Search right
                else:
                    l = mid + 1

        return -1

        # Time: O(log(n))
        # Space: O(1)