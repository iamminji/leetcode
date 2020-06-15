# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recursive(self, start, end, nums):
        if start > end:
            return None
        mid = (start + end) // 2

        tree = TreeNode(nums[mid])
        tree.left = self.recursive(start, mid - 1, nums)
        tree.right = self.recursive(mid + 1, end, nums)
        return tree

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if len(nums) == 0:
            return None

        mid = len(nums) // 2
        tree = TreeNode(nums[mid])

        tree.left = self.recursive(0, mid - 1, nums)
        tree.right = self.recursive(mid + 1, len(nums) - 1, nums)
        return tree


if __name__ == '__main__':
    from common import pp as _
    solution = Solution()
    tree = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(_.FullBinaryTreeNodePrettyPrinter.pp(tree))

