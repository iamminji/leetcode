# 77. Combinations
# https://leetcode.com/problems/combinations/

from typing import List
from copy import copy


class Solution:

    def helper(self, result, nums, start, end, i):

        if i == len(nums):
            result.append(copy(nums))
            return

        if start <= end:
            nums[i] = start
            self.helper(result, nums, start + 1, end, i + 1)
            self.helper(result, nums, start + 1, end, i)

        return

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        res = [0 for _ in range(k)]

        self.helper(result, res, 1, n, 0)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(5, 3))
    # assert sol.combine(4, 2) == [
    #     [2, 4],
    #     [3, 4],
    #     [2, 3],
    #     [1, 2],
    #     [1, 3],
    #     [1, 4],
    # ]
