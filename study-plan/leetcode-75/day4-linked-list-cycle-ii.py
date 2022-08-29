# https://leetcode.com/problems/linked-list-cycle-ii/
# 142. Linked List Cycle II

from typing import Optional
from common.leetcodeds import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow, fast = head, head
        cycle = False

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cycle = True
                break

        if not cycle:
            return None

        while head != slow:
            head = head.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    node = ListNode(3)
    node.next = ListNode(2)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(-4)
    node.next.next.next.next = node.next
    sol = Solution()
    print(sol.detectCycle(node))
