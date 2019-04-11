# 701. Insert into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # val 이라는 값이 들어올 때 TreeNode 에 위치시키는 문제다.
    # 이 때 Tree는 BinaryTree다.
    def helper(self, node, val):

        # leaf node 에 위치시키도록 했다.
        # 바이너리 트리이기 때문에 값 비교하면서 가장 하단 까지 내려가면 된다.
        if node is None:
            return

        if node.val < val:
            if node.right is not None:
                self.helper(node.right, val)
            else:
                node.right = TreeNode(val)
                return
        else:
            if node.left is not None:
                self.helper(node.left, val)
            else:
                node.left = TreeNode(val)
                return

        return

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.helper(root, val)
        return root
