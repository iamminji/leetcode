# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# 1448. Count Good Nodes in Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root.val, root))

        result = 0
        while queue:
            mx, node = queue.popleft()
            if node.val >= mx:
                result += 1

            if node.left is not None:
                queue.append((max(mx, node.val), node.left))

            if node.right is not None:
                queue.append((max(mx, node.val), node.right))

        return result
