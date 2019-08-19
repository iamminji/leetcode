# 1161. Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque()
        d = defaultdict(int)
        queue.append((1, root))

        while len(queue) > 0:
            depth, node = queue.popleft()
            d[depth] += node.val

            if node.left is not None:
                queue.append((depth + 1, node.left))

            if node.right is not None:
                queue.append((depth + 1, node.right))

        mv = max(d.values())
        res = float("inf")

        for k, v in d.items():
            if v == mv:
                res = min(res, k)

        return res
