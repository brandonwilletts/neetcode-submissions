# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(self.mergeTwoLists(l1, l2))
            
            lists = merged_list

        return lists[0]
        

    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy

        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        
        if head1:
            curr.next = head1
        elif head2:
            curr.next = head2

        return dummy.next

        # Time: O(n log(k))
        # Space: O(1)