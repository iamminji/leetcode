# 2385. Amount of Time for Binary Tree to Be Infected
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
from typing import Optional
from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, value, graph, result, visited):

        if value not in graph:
            return

        if value in visited:
            return

        visited.add(value)

        for v in graph[value]:
            if v in visited:
                continue
            result[v] = result[value] + 1
            self.dfs(v, graph, result, visited)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        # graph 로 바꾸기
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node is None:
                continue
            if node.left is not None:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right is not None:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                queue.append(node.right)

        result = defaultdict(int)
        visited = set()
        visited.add(start)
        for value in graph[start]:
            result[value] = 1

        for value in graph[start]:
            self.dfs(value, graph, result, visited)

        if not result:
            return 0
        return max(result.values())


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(6)

    root.left = TreeNode(5)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(2)

    root2 = TreeNode(1)
    print(sol.amountOfTime(root2, 1))
