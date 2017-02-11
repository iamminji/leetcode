# https://leetcode.com/problems/most-frequent-subtree-sum/

from collections import Counter


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.counter = list()
        self.helper(root)
        return find_most_frequent_data(self.counter)

    def helper(self, node):
        if node.left is None and node.right is None:
            self.counter.append(node.val)
            return node.val
        if node.left is not None:
            left = self.helper(node.left)
        else:
            left = 0
        if node.right is not None:
            right = self.helper(node.right)
        else:
            right = 0

        total = left + right + node.val
        self.counter.append(total)
        return total


def find_most_frequent_data(data):
    counter = Counter(data)
    max_count = max(counter.values())
    result = list()
    for k, v in counter.items():
        if v == max_count:
            result.append(k)
    return result
