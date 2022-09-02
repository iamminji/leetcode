# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# 637. Average of Levels in Binary Tree

from typing import Optional, List
from common.leetcodeds import TreeNode
from collections import deque, defaultdict


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append((0, root))
        result = []
        count = defaultdict(int)

        while queue:
            depth, node = queue.popleft()
            if depth >= len(result):
                result.append(node.val)
            else:
                result[depth] += node.val

            count[depth] += 1

            if node.left is not None:
                queue.append((depth + 1, node.left))
            if node.right is not None:
                queue.append((depth + 1, node.right))

        for idx in range(len(result)):
            result[idx] /= count[idx]

        return result
