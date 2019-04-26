# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = head
        length = 1
        while dummy is not None:
            dummy = dummy.next
            length += 1

        dummy = ListNode(0)
        dummy.next = head
        fake_dummy2 = dummy
        i = 1
        while i < length - n:
            dummy = dummy.next
            i += 1

        if dummy.next is not None:
            dummy.next = dummy.next.next

        return fake_dummy2.next
