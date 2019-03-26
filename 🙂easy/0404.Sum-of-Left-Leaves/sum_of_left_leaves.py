# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 트리에서 좌측 리프 노드의 값들만 전부 합산해서 리턴하는 문제다.
    def dfs(self, node: TreeNode, pos: str):

        if node.left is None and node.right is None:
            return node.val if pos == "L" else 0

        r = 0
        if node.left is not None:
            r += self.dfs(node.left, "L")

        if node.right is not None:
            r += self.dfs(node.right, "R")
        return r

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # 자식 노드가 없다면
        if root.left is None and root.right is None:
            return 0

        # 부모 노드가 좌측인지, 우측인지 함께 dfs 에서 넘겨 준다.
        # 그래서 리프 노드일 경우에 넘어온 부모 노드가 좌측일 경우에만 합산하면 된다.

        res = 0
        if root.left is not None:
            res += self.dfs(root.left, "L")

        if root.right is not None:
            res += self.dfs(root.right, "R")

        return res
