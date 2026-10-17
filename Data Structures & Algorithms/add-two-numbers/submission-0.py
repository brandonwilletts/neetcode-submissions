# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Get total
        str1, str2 = "", ""

        while l1:
            str1 = str(l1.val) + str1
            l1 = l1.next
        
        while l2:
            str2 = str(l2.val) + str2
            l2 = l2.next

        total = int(str1) + int(str2)
        total_str = str(total)

        # Construct linked list from total
        dummy = ListNode(0, None)
        curr = dummy

        for ch in total_str[::-1]:
            curr.next = ListNode(int(ch), None)
            curr = curr.next
        
        return dummy.next
        
        # Time: O(n)
        # Space: O(n)