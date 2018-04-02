# 808. Soup Servings
# https://leetcode.com/problems/soup-servings/description/

op = [[100, 0], [75, 25], [50, 50], [25, 75]]


class Solution:
    def dfs(self, A, B, visited):
        if A <= 0 and B <= 0:
            return 0.5
        if A <= 0:
            return 1
        if B <= 0:
            return 0

        if (A, B) in visited:
            return visited[(A, B)]

        r = 0
        for o in op:
            r += self.dfs(A - o[0], B - o[1], visited)

        visited[(A, B)] = 0.25 * r
        return visited[(A, B)]

    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        visited = {}

        if N > 4800:
            return 1
        res = self.dfs(N, N, visited)
        return res
