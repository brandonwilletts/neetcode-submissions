class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        l, r = 0, m - 1
        
        while True:

            # Define nums1 partition boundary
            i = (l + r) // 2
            left1 = nums1[i] if i >= 0 else float('-inf')
            right1 = nums1[i + 1] if (i + 1) < m else float('inf')

            # Define nums1 partition boundary
            j = ((m + n) // 2) - i - 2
            left2 = nums2[j] if j >= 0 else float('-inf')
            right2 = nums2[j + 1] if (j + 1) < n else float('inf')

            # Valid
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 != 0:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1 ,right2)) / 2

            # Invalid: Grow nums1
            elif (left1 > right2):
                r = i - 1

            # Invalid: Shrink nums1
            else:
                l = i + 1               
                      
        # Time: O(log(n))
        # Space: O(1)