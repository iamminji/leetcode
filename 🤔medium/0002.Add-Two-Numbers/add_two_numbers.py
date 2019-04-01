# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            s = carry + x + y
            carry = s // 10
            current.next = ListNode(s % 10)
            current = current.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    node = ListNode(3)
    node.next = ListNode(7)

    node2 = ListNode(9)
    node2.next = ListNode(2)

    r = sol.addTwoNumbers(node, node2)
    while r is not None:
        print(r.val)
        r = r.next
