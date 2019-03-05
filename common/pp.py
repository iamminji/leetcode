from collections import deque


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class FullBinaryTreeNodePrettyPrinter:
    """
        TreeNode의 모든 val 값을 찍어준다.
        이 때, TreeNode 는 full binary tree 이다.

        (우측 노드를 찍을 때 좌측 노드 값이 없으면 None / 좌측 노드 찍고 우측 노드 없으면 그냥 패스)
        찍어주는 순서는 root -> left -> right
    """

    @classmethod
    def pp(cls, node):
        queue = deque()
        queue.append(node)
        ans = []

        while 0 < len(queue) != queue.count(None):
            n = queue.popleft()
            if n is not None:
                ans.append(n.val)
                queue.append(n.left)
                queue.append(n.right)
            else:
                ans.append(None)
        return ans
