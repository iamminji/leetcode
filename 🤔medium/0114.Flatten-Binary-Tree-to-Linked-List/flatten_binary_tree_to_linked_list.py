# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# 114. Flatten Binary Tree to Linked List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 왼쪽 노드의 오른쪽 끝에 현재 노드의 오른쪽 트리를 전부 붙이고
        # 현재 노드의 오른쪽 노드로 다시 진행한다.

        while root is not None:
            if root.left is not None:
                tail = root.left
                while tail.right is not None:
                    tail = tail.right

                root.right, tail.right = root.left, root.right
                root.left = None
            root = root.right



