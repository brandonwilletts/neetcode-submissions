# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy
        start = end = head

        while end:
            # Advance end k nodes
            for _ in range(k - 1):
                end = end.next if end.next else None
                if end == None: break
            
            if end == None:
                break

            # Sever sublist and reverse
            end_next = end.next
            end.next = None

            curr.next = self.reverseList(start)

            # Reconnect reversed list to remaining list
            while curr.next:
                curr = curr.next

            curr.next = end_next
            start = end_next
            end = start

        return dummy.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
