class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        nums.sort()

        def backtrack(i: int, subset: list[int]):
            if i >= n:
                output.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # Don't include nums[i] or duplicates
            subset.pop()
            while (i + 1) < n and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])

        return output

        # Time: O(n * 2^n)
        # Space: O(n) - Max subset size, call stack