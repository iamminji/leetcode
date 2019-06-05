# 1038. Binary Search Tree to Greater Sum Tree
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # bst 이므로 가장 우측 부터 더해주면 된다.
    # right -> root -> left
    def helper(self, node, num):

        if node.left is None and node.right is None:
            node.val += num

        if node.right is not None:
            node.val += self.helper(node.right, num)

        if node.left is not None:
            return self.helper(node.left, node.val)

        return node.val

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.helper(root, 0)
        return root
