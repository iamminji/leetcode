# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        current = head
        while current is not None:
            node = current.next
            current.next = prev
            prev = current
            current = node

        return prev
