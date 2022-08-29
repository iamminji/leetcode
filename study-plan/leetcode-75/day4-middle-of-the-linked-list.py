# https://leetcode.com/problems/middle-of-the-linked-list/
# 876. Middle of the Linked List

from typing import Optional
from common.leetcodeds import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first, second = head, head

        if head.next is None:
            return head

        while second is not None and second.next is not None:
            first = first.next
            second = second.next.next

        return first

