from collections import deque
from common.leetcodeds import *


class FullBinaryTreeNodePrettyPrinter:
    """
        TreeNode의 모든 val 값을 찍어준다.
        이 때, TreeNode 는 full binary tree 이다.

        (우측 노드를 찍을 때 좌측 노드 값이 없으면 None / 좌측 노드 찍고 우측 노드 없으면 그냥 패스)
        찍어주는 순서는 root -> left -> right
    """

    @classmethod
    def pp(cls, node: TreeNode):
        queue = deque()
        queue.append(node)
        ans = []

        while len(queue) != queue.count(None):
            n = queue.popleft()
            if n is not None:
                ans.append(n.val)
                queue.append(n.left)
                queue.append(n.right)
            else:
                ans.append(None)
        print(ans)


def list_to_ListNode(l: list) -> ListNode:
    dummy = start = ListNode()
    for val in l:
        start.next = ListNode(val)
        start = start.next

    return dummy.next


if __name__ == '__main__':
    sample = TreeNode(1)
    sample.left = TreeNode(2)
    sample.right = TreeNode(3)
    sample.left.left = TreeNode(5)
    sample.right.right = TreeNode(7)

    # [1, 2, 3, 5, None, None, 7]
    FullBinaryTreeNodePrettyPrinter.pp(sample)

    sample1 = list_to_ListNode([1, 2, 3, 4, 5])
    while sample1 is not None:
        print(sample1.val)
        sample1 = sample1.next
