# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0, None)
        curr = dummy

        while l1 or l2 or carry:
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val

            sum_digits = l1_val + l2_val + carry
            carry = sum_digits // 10
            digit = sum_digits % 10

            curr.next = ListNode(digit, None)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next

        # Time: O(min(m, n))
        # Space: O(1) - Output linked list doesn't count as aux memory