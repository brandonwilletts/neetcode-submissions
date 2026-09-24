class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, a in enumerate(nums):
            # If offset is same as previous, continue
            if i > 0 and a == nums[i - 1]:
                continue
            
            # If offset positive, no further solutions
            if a > 0:
                break

            # Two pointer squeeze to find three sum
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                curr_sum = a + nums[l] + nums[r]

                if curr_sum == 0:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip past duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1

        return output