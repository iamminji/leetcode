# 86. Partition List
# https://leetcode.com/problems/partition-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if head is None:
            return None

        result = ListNode()
        dummy = result
        ptr = None
        while head is not None:
            if head.val < x:
                result.next = ListNode(head.val)
                result = result.next
            else:
                if ptr is None:
                    ptr = head
            head = head.next

        while ptr is not None:
            if x <= ptr.val:
                result.next = ListNode(ptr.val)
                result = result.next
            ptr = ptr.next

        return dummy.next
