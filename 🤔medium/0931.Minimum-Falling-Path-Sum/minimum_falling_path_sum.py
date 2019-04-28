# 931. Minimum Falling Path Sum
# https://leetcode.com/problems/minimum-falling-path-sum/

from typing import List


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:

        for i in range(1, len(A)):
            for j in range(len(A)):
                if j == 0:
                    A[i][j] = min(A[i - 1][j], A[i - 1][j + 1]) + A[i][j]
                elif j == len(A) - 1:
                    A[i][j] = min(A[i - 1][j - 1], A[i - 1][j]) + A[i][j]
                else:
                    A[i][j] = min(A[i - 1][j - 1], A[i - 1][j], A[i - 1][j + 1]) + A[i][j]

        return min(A[len(A) - 1])


if __name__ == '__main__':
    sol = Solution()
    assert sol.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 12
