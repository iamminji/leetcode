# https://leetcode.com/contest/weekly-contest-306/problems/largest-local-values-in-a-matrix/
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        result = []
        for i in range(0, len(grid) - 2):
            inner = []
            for j in range(0, len(grid[i]) - 2):
                mv = 0
                for p in range(3):
                    for q in range(3):
                        mv = max(mv, grid[i + p][j + q])
                inner.append(mv)
            result.append(inner)
        return result


if __name__ == '__main__':
    sol = Solution()
    grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    print(sol.largestLocal(grid))

    grid2 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    print(sol.largestLocal(grid2))
