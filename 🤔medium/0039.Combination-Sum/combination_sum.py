# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

from typing import List
from copy import copy


class Solution:

    def dfs(self, target, candidates, result, candi):

        if target == 0:
            return True
        elif target < 0:
            return False

        for num in candidates:
            if candi and candi[-1] > num:
                continue
            r = copy(candi)
            r.append(num)
            if self.dfs(target - num, candidates, result, r):
                result.append(r)

        return False

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)
        result = []
        self.dfs(target, candidates, result, [])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))
    print(sol.combinationSum([2, 3, 5], 8))
