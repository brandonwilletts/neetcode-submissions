class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        n = len(nums)
        nums.sort()

        def dfs(i: int, subset: list[int]):
            if i >= n:
                return

            # Include nums[i]
            subset.append(nums[i])
            output.append(subset.copy())
            dfs(i + 1, subset)

            # Don't include nums[i] or duplicates
            subset.pop()
            while (i + 1) < n and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, subset)

        dfs(0, [])

        return output

        # Time: O(n * 2^n)
        # Space: O(n) - Max subset size, call stack