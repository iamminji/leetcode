# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # binary tree의 최소 depth 를 리턴하는 문제다.
    def dfs(self, node: TreeNode, d: int):

        # dfs 로 depth 를 다 확인한다.
        if node.left is None and node.right is None:
            return d

        d1, d2 = float("inf"), float("inf")
        if node.left is not None:
            d1 = self.dfs(node.left, d + 1)

        if node.right is not None:
            d2 = self.dfs(node.right, d + 1)

        return min(d1, d2)

    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        return self.dfs(root, 1)
