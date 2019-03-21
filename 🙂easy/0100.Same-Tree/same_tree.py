# 100. Same Tree
# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Tree 2개 같은지 여부를 판단하는 문제다.
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is not None and q is not None:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif p is None and q is None:
            return True
        return False
