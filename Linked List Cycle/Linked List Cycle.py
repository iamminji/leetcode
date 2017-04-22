# https://leetcode.com/problems/linked-list-cycle/#/description

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        t, h = head, head
        if h is None:
            return False
        while True:
            h = h.next
            if h is None:
                return False
            h = h.next
            if h is None:
                return False
            t = t.next
            if h.val == t.val:
                return True
