# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.a
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def helper(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return (left.val == right.val) and self.helper(left.right, right.left) and self.helper(right.left, left.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root, root)
