class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        lowest = min(nums[l], nums[r])

        while l <= r:
            # nums[l] is the lowest
            if nums[l] < nums[r]:  
                lowest = min(lowest, nums[l])
                break

            mid = (l + r) // 2
            lowest = min(lowest, nums[mid])

            # lowest is in right half
            if nums[mid] >= nums[l]:
                l = mid + 1
            # lowest is in left half
            else:
                r = mid - 1

        return lowest

        # Time: (log(n))
        # Space: O(1)