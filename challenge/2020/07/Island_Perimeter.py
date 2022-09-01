class Solution:

    def dfs(self, i, j, grid, cache):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
            return 1

        if grid[i][j] == 0:
            return 1

        if (i, j) in cache:
            return 0

        cache[(i, j)] = True

        ans = 0
        ans += self.dfs(i, j - 1, grid, cache)
        ans += self.dfs(i, j + 1, grid, cache)
        ans += self.dfs(i + 1, j, grid, cache)
        ans += self.dfs(i - 1, j, grid, cache)

        return ans

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        cache = dict()
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ans += self.dfs(i, j, grid, cache)

        return ans
