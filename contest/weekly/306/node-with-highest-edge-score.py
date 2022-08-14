# https://leetcode.com/contest/weekly-contest-306/problems/node-with-highest-edge-score/
from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        graph = [0 for _ in range(len(edges))]

        for i in range(len(edges)):
            graph[edges[i]] += i

        cur_max = -1
        cur_node = -1
        for i in range(len(graph)):
            if cur_max < graph[i]:
                cur_max = graph[i]
                cur_node = i
            elif cur_max == graph[i]:
                cur_node = min(cur_node, i)

        return cur_node


if __name__ == '__main__':
    sol = Solution()
    print(sol.edgeScore([1, 0, 0, 0, 0, 7, 7, 5]))
    print(sol.edgeScore([2, 0, 0, 2]))
