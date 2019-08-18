# 617. Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def dfs(self, t1, t2):
        t1.val += t2.val

        if t1.left is not None and t2.left is not None:
            self.mergeTrees(t1.left, t2.left)

        if t1.right is not None and t2.right is not None:
            self.mergeTrees(t1.right, t2.right)

        if t1.left is None and t2.left is not None:
            t1.left = t2.left

        if t1.right is None and t2.right is not None:
            t1.right = t2.right

        return t1

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if t1 is None and t2 is None:
            return None

        if t1 is not None and t2 is None:
            return t1
        if t1 is None and t2 is not None:
            return t2

        return self.dfs(t1, t2)
