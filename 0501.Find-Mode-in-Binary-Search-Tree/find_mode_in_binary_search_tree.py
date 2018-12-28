# 501. Find Mode in Binary Search Tree
# https://leetcode.com/problems/find-mode-in-binary-search-tree/

from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = defaultdict(int)
        if root is None:
            return []
        self.result[self.helper(root)] += 1
        if self.result:
            max_count = max(self.result.values())
        real_result = []
        for k, v in self.result.items():
            if v == max_count:
                real_result.append(k)
        return real_result

    def helper(self, node):

        if node.left is not None:
            self.result[self.helper(node.left)] += 1

        if node.right is not None:
            self.result[self.helper(node.right)] += 1

        return node.val
