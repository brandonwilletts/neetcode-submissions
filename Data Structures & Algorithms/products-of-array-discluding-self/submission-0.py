class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length
        postfix = 1

        # Calculate prefix product
        for i in range(length):
            if i != 0: 
                output[i] = output[i-1] * nums[i-1]

        # Calculate postfix product
        for i in range(length - 1, -1, -1):
            if i != (length - 1):
                postfix *= nums[i+1]
                output[i] = output[i] * postfix

        return output