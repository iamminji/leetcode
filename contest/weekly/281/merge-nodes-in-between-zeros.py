# https://leetcode.com/contest/weekly-contest-281/problems/merge-nodes-in-between-zeros/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        node = result
        val = 0

        while head is not None:
            if head.val == 0:
                node.next = ListNode(val)
                node = node.next
                val = 0
            else:
                val += head.val
            head = head.next

        return result.next.next
