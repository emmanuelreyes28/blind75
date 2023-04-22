# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time O(n) | Space O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current:
            # store the next node in the og list since we will overwrite current.next
            nxt = current.next
            # point the next value to the previous essential flipping its pointer
            current.next = previous
            # update previous to be current node
            previous = current
            # update current to be nxt node
            current = nxt

        return previous
