# 797. All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/description/


class Solution:

    def dfs(self, graph, depth, path, result):

        if depth == len(graph) - 1:
            result.append(path)
            return

        for i in graph[depth]:
            self.dfs(graph, i, path + [i], result)
        return

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(graph, 0, [0], result)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.allPathsSourceTarget([[1, 2], [3], [3], []]))
    print(sol.allPathsSourceTarget([[1, 2], [2], [3], []]))
