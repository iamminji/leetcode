# https://leetcode.com/problems/reverse-linked-list/
# 206. Reverse Linked List

from typing import Optional
from common.leetcodeds import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        start = dummy = ListNode()

        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next

        while stack:
            start.next = ListNode(stack.pop())
            start = start.next

        return dummy.next

    def reverseList_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev, cur = None, head
        while head is not None:
            head = head.next
            cur.next = prev
            prev = cur
            cur = head
        return prev


if __name__ == '__main__':
    sol = Solution()
    cur = node = ListNode()
    for i in range(1, 6):
        node.next = ListNode(i)
        node = node.next

    print(sol.reverseList_2(cur.next))
