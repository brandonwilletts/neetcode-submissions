# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = end = dummy

        while end:
            # Advance end by k nodes
            for _ in range(k):
                end = end.next if end.next else None
                if end == None: break
            
            if end == None:
                break

            # Reverse sublist
            next_start = end.next
            reversed_tail = curr.next

            curr.next = self.reverse_k_nodes(curr.next, k)

            # Reconnect reversed list to remaining list
            curr = reversed_tail
            curr.next = next_start
            
            end = curr

        return dummy.next

    def reverse_k_nodes(self, head: Optional[ListNode], k) -> Optional[ListNode]:
        curr, prev = head, None

        while curr and k > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1
        
        return prev

    # Time: O(n)
    # Space: O(1)
