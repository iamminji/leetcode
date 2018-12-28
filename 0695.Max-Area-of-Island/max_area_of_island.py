# 695. Max Area of Island
# https://leetcode.com/problems/max-area-of-island/description/


class Solution:

    def dfs(self, grid, i, j, visited):

        if i < 0 or i >= len(grid[0]) or j < 0 or j >= len(grid):
            return 0

        if grid[j][i] == 0:
            return 0

        if (i, j) in visited:
            return 0

        visited.add((i, j))

        result = 1
        result += self.dfs(grid, i + 1, j, visited)
        result += self.dfs(grid, i - 1, j, visited)
        result += self.dfs(grid, i, j + 1, visited)
        result += self.dfs(grid, i, j - 1, visited)

        return result

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        visited = set()
        res = []
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                r = self.dfs(grid, i, j, visited)
                res.append(r)

        return max(res) if res else 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAreaOfIsland([[1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
                               [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                               [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                               [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
                               [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                               [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
                               [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                               [1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
                               [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                               [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]))
