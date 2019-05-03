# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/


from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Tree에서 같은 level 의 node 끼리 동일한 리스트에 넣어, 전체 리스트를 리턴하는 문제다.
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        queue = deque()
        queue.append((root, 0))

        res = []
        while len(queue) > 0:
            node, depth = queue.popleft()
            if len(res) <= depth:
                res.append([node.val])
            else:
                res[depth].append(node.val)

            if node.left is not None:
                queue.append((node.left, depth + 1))

            if node.right is not None:
                queue.append((node.right, depth + 1))

        return res


if __name__ == '__main__':
    sol = Solution()
    n = TreeNode(3)
    n.left = TreeNode(9)
    n.right = TreeNode(20)
    n.right.left = TreeNode(15)
    n.right.right = TreeNode(7)

    print(sol.levelOrder(n))
