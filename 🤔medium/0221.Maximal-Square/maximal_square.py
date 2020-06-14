# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if len(matrix) == 0:
            return 0

        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        dp[0] = [1 if x == "1" else 0 for x in matrix[0]]

        for i in range(0, len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = 1
            else:
                dp[i][0] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        result = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                result = max(result, dp[i][j] * dp[i][j])

        return result
