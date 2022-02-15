# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        if root is None:
            return 0

        res = 1
        queue.append((root, res))

        while queue:
            node, depth = queue.popleft()
            res = max(res, depth)

            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))

        return res
