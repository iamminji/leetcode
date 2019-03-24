# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/


from typing import List
from copy import copy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # binary tree 에서 모든 leaf 노드로 다다르는 순서들의 val 값이 '->' 기호를 통해 이어져서
    # 리스트로 출력해야 하는 문제다.
    def helper(self, node, p, r):
        if node is None:
            return

        # 현재 노드의 값을 넣는다.
        p.append(str(node.val))

        # 자식 노드가 없으면 leaf 노드다.
        # 여태까지 축적했던 결과 값 path list 를 join 해서 결과 값 r에 넣는다.
        # 최종 결과 값이 된다.
        if node.left is None and node.right is None:
            r.append("->".join(p))
            return

        # 각 자식 노드를 순회한다.
        # 이 때 기존 path list와 다른 path list이므로 copy 함수를 써서
        # object copy 를 피했다.

        if node.left is not None:
            p1 = copy(p)
            self.helper(node.left, p1, r)

        if node.right is not None:
            p2 = copy(p)
            self.helper(node.right, p2, r)

        return

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]

        res = []
        # 재귀로 각 노드를 모두 탐색한다.
        # 각 arguments 는 노드, 여태까지 진행했던 순서, 결과 값 이다.
        self.helper(root, [], res)
        return res
