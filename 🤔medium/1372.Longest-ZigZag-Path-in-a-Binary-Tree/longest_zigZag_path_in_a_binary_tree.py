# 1372. Longest ZigZag Path in a Binary Tree
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "Node(%s)" % self.val


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        queue = deque()

        if root.left is not None:
            queue.append((1, True, root.left))

        if root.right is not None:
            queue.append((1, False, root.right))

        ans = 0

        while queue:
            step, from_left, node = queue.popleft()

            if node is None:
                continue

            ans = max(step, ans)
            if from_left:
                queue.append((1, True, node.left))
                queue.append((step + 1, False, node.right))
            else:
                queue.append((step + 1, True, node.left))
                queue.append((1, False, node.right))

        return ans


if __name__ == '__main__':
    node = TreeNode(1)
    node.right = TreeNode(2)
    node.right.left = TreeNode(3)
    node.right.right = TreeNode(4)
    node.right.right.right = TreeNode(5)

    sol = Solution()
    print(sol.longestZigZag(node))

    node2 = TreeNode(1)
    node2.left = TreeNode(2)
    node2.right = TreeNode(3)
    node2.left.right = TreeNode(4)
    node2.left.right.left = TreeNode(5)
    print(sol.longestZigZag(node2))
