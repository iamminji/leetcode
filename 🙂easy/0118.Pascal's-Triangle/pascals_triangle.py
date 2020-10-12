# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append([1 for _ in range(1, i + 2)])

        for i in range(2, numRows):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result
