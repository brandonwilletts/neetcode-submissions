class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()

        def dfs(i: int, subset: list[int], total: int) -> None:
            if total == target and subset not in output:
                output.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # Include candidates[i]
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])

            # Don't include candidates[i]
            subset.pop()
            while (
                i + 1 < len(candidates) and 
                candidates[i] == candidates[i + 1]
                ): i += 1
            dfs(i + 1, subset, total)
        
        dfs(0, [], 0)
        return output

        # Time: O(n * 2^n)
        # Space: O(n) - Max size of subset, call stack
