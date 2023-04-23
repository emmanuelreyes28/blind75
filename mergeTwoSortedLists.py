# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node and a tail pointer and initialize them to the same node.
        dummy = ListNode()
        tail = dummy

        # traverse both the input lists simultaneously until either of them becomes None.
        while list1 and list2:
            # check which of the two nodes has the smaller value since we want to sort the merged list
            if list1.val < list2.val:
                # make next tail node point to the list1 node since it is the smallest
                tail.next = list1
                list1 = list1.next  # update list to grab next node in ll
            else:
                tail.next = list2
                list2 = list2.next
            # update the tail pointer to the next node.
            tail = tail.next

        #  check if either list still has any remaining nodes, and append them to the end of the merged list.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
