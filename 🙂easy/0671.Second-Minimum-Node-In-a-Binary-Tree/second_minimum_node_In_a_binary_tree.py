# 671. Second Minimum Node In a Binary Tree
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        queue = deque()
        val = [float("inf"), float("inf")]

        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()
            if node is not None:
                val[0] = min(node.val, val[0])
                if val[0] < node.val < val[1]:
                    val[1] = node.val

                queue.append(node.left)
                queue.append(node.right)

        return val[1] if val[1] != float("inf") else -1
