# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# 589. N-ary Tree Preorder Traversal

from typing import List
from common.leetcodeds import Node


class Solution:
    def dfs(self, node, result):

        if node is None:
            return

        result.append(node.val)

        if node.children is None:
            return

        for child in node.children:
            self.dfs(child, result)

    # TODO iteration 으로도 풀기
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = [root.val]
        for node in root.children:
            self.dfs(node, result)
        return result
