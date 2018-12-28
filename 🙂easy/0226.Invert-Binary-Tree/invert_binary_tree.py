# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        queue = list()
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop()
            if node is None:
                continue
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
        return root
