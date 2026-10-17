class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       
        # Detect cycle
        fast = slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        # Find start of cycle (duplicate)
        fast = 0

        while True:
            fast = nums[fast]
            slow = nums[slow]

            if fast == slow:
                return fast

        # Time: O(n)
        # Space: O(1)