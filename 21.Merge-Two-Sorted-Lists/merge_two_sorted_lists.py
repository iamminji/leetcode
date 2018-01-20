# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = ListNode(-1)
        temp = result

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        if l1 is not None:
            temp.next = l1
        elif l2 is not None:
            temp.next = l2

        return result.next
