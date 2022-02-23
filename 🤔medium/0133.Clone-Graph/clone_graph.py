# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/
from collections import defaultdict, deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return None

        g = dict()

        color = defaultdict(int)
        queue = deque()
        queue.append(node)

        while queue:
            inner = queue.popleft()
            if color[inner.val] == 2:
                continue
            if color[inner.val] == 0:
                g[inner.val] = Node(inner.val)
            color[inner.val] = 1

            for n in inner.neighbors:
                if color[n.val] == 0:
                    g[n.val] = Node(n.val)
                    color[n.val] = 1
                g[inner.val].neighbors.append(g[n.val])
                queue.append(n)
            color[inner.val] = 2

        return g[node.val]
