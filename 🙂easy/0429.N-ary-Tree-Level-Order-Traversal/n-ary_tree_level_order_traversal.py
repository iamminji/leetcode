# 429. N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    # 트리 노드에서 같은 depth 에 있는 노드 값들은 같은 리스트에 넣어,
    # 전체 depth 순으로 리스트를 만드는 문제다.
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        queue = []
        res = []

        if root is None:
            return res

        # 루트 노드를 넣어준다.
        queue.append(root)

        # bfs 로 진행하되 노드의 자식 값들은 같은 depth 이므로
        # 같은 리스트에 담기 위해 for loop를 돌아준다.

        # 큰 그림은 다음과 같다.
        # 큐 두개를 써서 하나는 현재 노드들의 값을 넣어주는 용이고 나머지 하나는 그 노드들의 자식 노드들을 위한 용이다.
        # 노드는 여러개의 자식을 가질 수 있는데 그 자식들의 바로 밑의 자식들은 서로 같은 depth (level) 을 갖고 있다.
        # 이를 위해서 큐 (리스트) 두 개를 쓰는 것이다.

        # 즉, 코드로 보자면 queue 라는 리스트는 같은 level 의 노드들의 값들을 리스트에 넣어주는 것이고
        # 그 같은 level의 노드들의 자식들을 위해 temp 라는 리스트를 따로 만들어서 넣어주고 그 리스트를 다시 순회해서 각 노드들의 자식들을 queue 라는 리스트에 넣어준다.

        while len(queue) > 0:
            temp = []
            r = []
            for node in queue:
                r.append(node.val)
                temp.append(node)
            res.append(r)
            queue = []
            for node in temp:
                for child in node.children:
                    queue.append(child)

        return res
