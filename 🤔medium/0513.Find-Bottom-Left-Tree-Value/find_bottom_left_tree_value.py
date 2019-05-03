# 513. Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 가장 좌측 하단의 노드를 리턴하는 문제다.
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # 루트 -> 우측 -> 좌측 순으로 순회하면 된다.
        queue = deque()
        queue.append(root)

        res = -1
        while len(queue) > 0:
            node = queue.popleft()
            if node is None:
                continue
            res = node.val
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)

        return res
