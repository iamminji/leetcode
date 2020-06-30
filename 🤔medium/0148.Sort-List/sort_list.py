# 148. Sort List
# https://leetcode.com/problems/sort-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "ListNode(%s)" % self.val


class Solution:

    def sortList(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        middle = head
        fast = head.next
        slow = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            middle = middle.next

        middle.next = None

        node1 = self.sortList(head)
        node2 = self.sortList(slow)

        return self.merge(node1, node2)

    def merge(self, left, right):

        print(left, right)

        if left is None:
            return right

        if right is None:
            return left

        if left.val < right.val:
            left.next = self.merge(left.next, right)
            return left
        else:
            right.next = self.merge(left, right.next)
            return right


if __name__ == '__main__':
    node = ListNode(3)
    node.next = ListNode(1)
    node.next.next = ListNode(2)
    node.next.next.next = ListNode(5)
    node.next.next.next.next = ListNode(9)
    node.next.next.next.next.next = ListNode(4)

    sol = Solution()
    node = sol.sortList(node)

    while node is not None:
        print(node.val)
        node = node.next
