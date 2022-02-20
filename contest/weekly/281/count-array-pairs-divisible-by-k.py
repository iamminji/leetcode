from typing import List
from collections import defaultdict


# TLE
class Solution:
    def dfs(self, node, graph, visited):

        r = 0
        if node not in graph:
            return r

        if node in visited:
            return r

        visited.add(node)
        for n in graph[node]:
            r += self.dfs(n, graph, visited) + 1
        return r

    def countPairs(self, nums: List[int], k: int) -> int:
        graph = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] * nums[j]) % k == 0:
                    graph[nums[i]].append(nums[j])

        result = 0
        visited = set()
        for node in graph:
            if node not in visited:
                result += self.dfs(node, graph, visited)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPairs([1, 2, 3, 4, 5], 2))
    print(solution.countPairs([8, 10, 2, 5, 9, 6, 3, 8, 2], 6))
