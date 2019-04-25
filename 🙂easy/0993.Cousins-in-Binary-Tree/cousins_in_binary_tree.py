# 993. Cousins in Binary Tree
# https://leetcode.com/problems/cousins-in-binary-tree/
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 각 노드의 val 이 유니크할 때, x 노드와 y 노드가 사촌인 경우 true 를 리턴하는 문제다.
    # 사촌이어야 하기 때문에 부모 노드는 달라야 한다.
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        queue = deque()
        queue.append((root, 0))
        l, r = -1, -1

        while len(queue) > 0 or (l == -1 and r == -1):
            node, depth = queue.popleft()

            if node is None:
                continue

            if node.left is not None and node.right is not None:
                # 부모 노드가 같은 경우 예외 처리
                if node.left.val == x and node.right.val == y:
                    return False
                if node.right.val == x and node.left.val == y:
                    return False

            # depth 갱신
            if node.val == x:
                l = depth
            if node.val == y:
                r = depth

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        return l == r if l != -1 and r != -1 else False
