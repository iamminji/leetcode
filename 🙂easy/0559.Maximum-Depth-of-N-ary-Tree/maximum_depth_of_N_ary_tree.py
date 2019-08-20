# 559. Maximum Depth of N-ary Tree
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if root is None:
            return 0

        queue = deque()
        queue.append((root, 1))

        res = 0
        while len(queue) > 0:
            node, depth = queue.popleft()

            res = max(res, depth)

            if node.children is not None:
                for child in node.children:
                    queue.append((child, depth + 1))

        return res
