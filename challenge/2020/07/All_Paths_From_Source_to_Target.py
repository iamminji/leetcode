from collections import defaultdict
from typing import List


class Solution:

    def dfs(self, node, graph, ans, visited, result):

        if node not in graph:
            result.append(ans)
            return

        for n in graph[node]:
            self.dfs(n, graph, ans + [n], visited, result)

        return

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        visited = dict()
        nodes = defaultdict(list)

        for i, g in enumerate(graph):
            if g:
                nodes[i] = g

        self.dfs(0, nodes, [0], visited, result)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.allPathsSourceTarget([[1, 2], [3], [3], []]))
    print(sol.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
