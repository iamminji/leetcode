# 109. Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TODO 다른 방식도 풀어보기
class Solution:

    def recursive(self, start, end, nums):
        if start > end:
            return None
        mid = (start + end) // 2

        tree = TreeNode(nums[mid])
        tree.left = self.recursive(start, mid - 1, nums)
        tree.right = self.recursive(mid + 1, end, nums)
        return tree

    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if head is None:
            return None

        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next

        mid = len(nums) // 2

        tree = TreeNode(nums[mid])
        tree.left = self.recursive(0, mid - 1, nums)
        tree.right = self.recursive(mid + 1, len(nums) - 1, nums)
        return tree
