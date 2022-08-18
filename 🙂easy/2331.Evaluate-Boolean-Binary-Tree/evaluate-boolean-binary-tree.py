# https://leetcode.com/problems/evaluate-boolean-binary-tree/
# 2331. Evaluate Boolean Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, node:TreeNode):
        if node is None:
            return False
        if node.val == 2:
            return self.dfs(node.left) or self.dfs(node.right)
        if node.val == 3:
            return self.dfs(node.left) and self.dfs(node.right)
        if node.val == 1:
            return True
        return False

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is not None:
            return self.dfs(root)
        # never reached
        return None
