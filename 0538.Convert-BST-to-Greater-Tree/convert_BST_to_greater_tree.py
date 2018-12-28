# 538. Convert BST to Greater Tree
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#     def __str__(self):
#         return '%s' % self.val


class Solution:

    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)

        return root
