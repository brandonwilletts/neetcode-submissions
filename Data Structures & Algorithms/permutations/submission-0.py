class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []
        nums_length = len(nums)

        def dfs():
            if len(subset) == nums_length:
                output.append(subset.copy())
                return
            
            # Loop through nums, skip if already added to subset
            for num in nums:
                if num not in subset:
                    # Include num
                    subset.append(num)
                    dfs()

                    # Don't include num
                    subset.pop()

        dfs()
        return output

        # Time: O(n!)
        # Space: O(n) - Max subset size, call stack
        