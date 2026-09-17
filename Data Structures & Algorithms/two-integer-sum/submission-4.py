class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            pair = target - num
            if pair in indices:
                return [indices[pair], i]
            indices[num] = i
