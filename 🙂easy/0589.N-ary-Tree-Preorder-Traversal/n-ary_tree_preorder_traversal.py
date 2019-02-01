# 589. N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# python 3

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:

    def __init__(self):
        self.result = []

    def _preorder(self, node):
        if len(node.children) == 0:
            self.result.append(node.val)
            return

        self.result.append(node.val)

        for n in node.children:
            self._preorder(n)

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if root is not None:
            self._preorder(root)

        return self.result
