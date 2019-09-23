# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/


from collections import deque, defaultdict
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        res = defaultdict(list)
        queue = deque()
        queue.append([0, root])

        while len(queue) > 0:
            level, node = queue.popleft()
            res[level].append(node.val)

            if node.left is not None:
                queue.append([level + 1, node.left])

            if node.right is not None:
                queue.append([level + 1, node.right])

        ans = []
        for k in res:
            ans.append(sum(res[k]) / len(res[k]))
        return ans
