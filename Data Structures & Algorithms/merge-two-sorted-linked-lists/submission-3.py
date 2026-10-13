# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        curr1, curr2 = list1, list2

        if curr1.val < curr2.val:
            head = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next
        
        curr_new = head

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr_new.next = curr1
                curr1 = curr1.next
            else:
                curr_new.next = curr2
                curr2 = curr2.next
            curr_new = curr_new.next
        
        if curr1:
            curr_new.next = curr1
        elif curr2:
            curr_new.next = curr2
        
        return head
        
        # Time: O(m + n)
        # Space: O(1)