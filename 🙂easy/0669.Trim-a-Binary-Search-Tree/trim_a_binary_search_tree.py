# 669. Trim a Binary Search Tree
# https://leetcode.com/problems/trim-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        if root is None:
            return root

        if L > root.val:
            return self.trimBST(root.right, L, R)

        if R < root.val:
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        return root