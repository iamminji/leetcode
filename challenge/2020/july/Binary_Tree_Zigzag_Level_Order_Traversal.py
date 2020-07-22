from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        if root is None:
            return None

        queue = deque()
        queue.append((root, 0))

        while queue:
            node, depth = queue.popleft()
            if len(result) <= depth:
                result.append([node.val])
            else:
                result[depth].append(node.val)

            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))

        for depth, _ in enumerate(result):
            if depth % 2 != 0:
                result[depth].reverse()

        return result
