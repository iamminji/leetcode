# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        while head is not None and head.val == val:
            head = head.next

        if head is None:
            return None

        prev, dummy = head, head.next
        while dummy is not None:
            if dummy.val == val:
                prev.next = dummy.next
                dummy = dummy.next
            else:
                prev = prev.next
                dummy = dummy.next

        return head
