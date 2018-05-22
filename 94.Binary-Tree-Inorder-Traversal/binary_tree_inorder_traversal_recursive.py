# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '%r' % self.val


class Solution(object):

    def helper(self, node, res):
        if node is None:
            return

        self.helper(node.left, res)
        res.append(node.val)
        self.helper(node.right, res)
        return

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        self.helper(root, res)

        return res


if __name__ == "__main__":
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)

    node.right = TreeNode(3)
    node.right.left = TreeNode(6)

    sol = Solution()
    print(sol.inorderTraversal(node))
