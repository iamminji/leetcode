# 1027. Longest Arithmetic Sequence
# https://leetcode.com/problems/longest-arithmetic-sequence/

from typing import List
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(int)
        result = 0

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                diff = A[i] - A[j]
                if (i, diff) in dp:
                    dp[(j, diff)] = dp[(i, diff)] + 1
                else:
                    dp[(j, diff)] = 2
                result = max(result, dp[(j, diff)])

        return result


if __name__ == '__main__':
    sol = Solution()

    assert sol.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]) == 4
    assert sol.longestArithSeqLength([9, 4, 7, 2, 10]) == 3
    assert sol.longestArithSeqLength([3, 6, 9, 12]) == 4
