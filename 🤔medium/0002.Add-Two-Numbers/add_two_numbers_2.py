# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        result = ListNode(0)
        dummy = result
        while l1 is not None or l2 is not None:
            lv1 = l1.val if l1 is not None else 0
            lv2 = l2.val if l2 is not None else 0

            v = lv1 + lv2 + c
            c, r = v // 10, v % 10

            dummy.next = ListNode(r)

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            dummy = dummy.next

        if c > 0:
            dummy.next = ListNode(c)

        return result.next
