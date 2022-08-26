# https://leetcode.com/problems/reverse-linked-list/
# 206. Reverse Linked List

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


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
        # TODO stack 사용 없이 풀어보기
        pass


if __name__ == '__main__':
    sol = Solution()
    cur = node = ListNode()
    for i in range(1, 6):
        node.next = ListNode(i)
        node = node.next

    print(sol.reverseList_2(cur.next))
