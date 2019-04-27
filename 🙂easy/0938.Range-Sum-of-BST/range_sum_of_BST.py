# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop()
            if node is None:
                continue
            if L <= node.val <= R:
                res += node.val

            if node.val <= R:
                queue.append(node.right)
            if node.val >= L:
                queue.append(node.left)

        return res
