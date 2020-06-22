# 1019. Next Greater Node In Linked List
# https://leetcode.com/problems/next-greater-node-in-linked-list/

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:

        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next

        ans = [0 for _ in range(len(nums))]
        stack = []

        idx = 0
        while idx < len(nums):
            while len(stack) > 0 and nums[idx] > stack[-1][1]:
                ans[stack.pop()[0]] = nums[idx]
            stack.append((idx, nums[idx]))
            idx += 1

        print(stack, ans)

        return ans


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(1)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(3)

    sol = Solution()
    print(sol.nextLargerNodes(node))
