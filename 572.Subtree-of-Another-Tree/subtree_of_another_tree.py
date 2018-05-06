# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '%r' % self.val


class Solution:

    def check(self, s_node, t_node):
        if s_node is None and t_node is None:
            return True
        if s_node is None or t_node is None:
            return False

        return s_node.val == t_node.val \
               and self.check(s_node.left, t_node.left) \
               and self.check(s_node.right, t_node.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if self.check(s, t):
            return True

        if s is not None:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        return False


if __name__ == "__main__":
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)

    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(3)

    sol = Solution()
    print(sol.isSubtree(s, t))
