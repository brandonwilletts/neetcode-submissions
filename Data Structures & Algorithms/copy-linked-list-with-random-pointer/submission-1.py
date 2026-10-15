"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Copy nodes and save to hashmap (original --> copy)
        copies = { None: None, }
        curr = head

        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        # Update next and random pointers
        curr = head

        while curr:
            copies[curr].next = copies[curr.next]
            copies[curr].random = copies[curr.random]
            curr = curr.next

        return copies[head]

        # Time: O(n)
        # Space: O(n)