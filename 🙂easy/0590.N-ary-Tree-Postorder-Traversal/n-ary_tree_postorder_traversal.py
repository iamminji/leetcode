# 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

# python3


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

    def _postorder(self, node):

        if len(node.children) == 0:
            self.result.append(node.val)
            return

        for n in node.children:
            self._postorder(n)

        self.result.append(node.val)

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if root is not None:
            self._postorder(root)

        return self.result
