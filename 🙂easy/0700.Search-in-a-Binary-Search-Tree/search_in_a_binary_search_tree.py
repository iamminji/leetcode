# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 바이너리 트리에서 val이 노드의 val 인 경우 해당 노드(정확히는 자식 노드를 포함, 부모 노드를 제외한 트리노드)를 리턴하는 문제다.
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 좌측이 현재 노드의 값 보다 작고 우측이 현재 노드의 값 부터 큰 것을 이용하여 풀면 된다.
        if root is None:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
