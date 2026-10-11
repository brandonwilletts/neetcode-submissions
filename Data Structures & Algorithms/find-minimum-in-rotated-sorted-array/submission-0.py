class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        lowest = min(nums[l], nums[r])

        while l <= r:
            mid = (l + r) // 2

            lowest = min(lowest, nums[mid])

            if nums[r] < nums[l]:
                # lowest is in right half
                if nums[r] < nums[mid]:
                    l = mid + 1
                # lowest is in left half
                else:
                    r = mid - 1
            
            else:
                # lowest is in left half
                if nums[l] < nums[mid]:
                    r = mid - 1
                # lowest is in right half
                else:
                    l = mid + 1

        return lowest

        # Time: (log(n))
        # Space: O(1)