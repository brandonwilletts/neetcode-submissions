class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(i: int, subset: List[int], total: int):
            if total == target:
                output.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            subset.append(nums[i])
            
            # Include nums[i]
            dfs(i, subset, total + nums[i])
            subset.pop()
        
            # Don't include nums[i]
            dfs(i + 1, subset, total)
            
        dfs(0, [], 0)
        
        return output

        # Time: O(2^n)
        # Space: O(n)
