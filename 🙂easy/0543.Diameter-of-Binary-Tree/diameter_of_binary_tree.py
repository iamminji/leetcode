# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '%s' % self.val


class Solution:

    def __init__(self):
        self.total = 0

    def dfs(self, node):

        if node is None:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.total = max(self.total, left + right)

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        res = self.dfs(root.left) + self.dfs(root.right)
        return max(res, self.total)


if __name__ == "__main__":
    """
              1
             / \
            2   3
           / \     
          4   5    
    """
    root = TreeNode(1)
    # root.right = TreeNode(3)
    # node = TreeNode(2)
    # node.left = TreeNode(4)
    # node.right = TreeNode(5)
    # root.left = node

    sol = Solution()
    print('###', sol.diameterOfBinaryTree(root))
