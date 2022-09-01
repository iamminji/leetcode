from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "TreeNode(val:%s)" % self.val


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        queue = deque()
        queue.append([root, 0])

        result = []

        while queue:
            node, depth = queue.popleft()

            if len(result) <= depth:
                result.append([node.val])
            else:
                result[depth].append(node.val)

            if node.left is not None:
                queue.append([node.left, depth+1])

            if node.right is not None:
                queue.append([node.right, depth+1])

        return result[::-1]


if __name__ == '__main__':
    # [3,9,20,null,null,15,7]
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)

    sol = Solution()
    print(sol.levelOrderBottom(node))
