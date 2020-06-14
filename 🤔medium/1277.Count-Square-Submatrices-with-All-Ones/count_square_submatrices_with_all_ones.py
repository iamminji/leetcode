# 1277. Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        dp[0] = matrix[0]
        for i in range(0, len(matrix)):
            dp[i][0] = matrix[i][0]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

        result = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                result += dp[i][j]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
    print(solution.countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1, 1]]))
