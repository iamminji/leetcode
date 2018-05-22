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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if root is None:
            return []
        stack = [root]
        node = root
        while len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            res.append(node.val)
            node = node.right
        res.pop()
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
