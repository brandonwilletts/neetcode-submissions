class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []

        def dfs(i: int):
            # Reached the end of nums --> append
            if i >= len(nums):
                output.append(subset.copy())
                return

            # Include num at index i
            subset.append(nums[i])
            dfs(i + 1)

            # Don't include num at index i
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return output

        # Time: O(n * 2^n)
        # Space: O(n) - Max size of subset, call stack