from typing import List
from copy import deepcopy


class Solution:

    def dfs(self, nums, i, inner, result):
        result.append(deepcopy(inner))
        for j in range(i, len(nums)):
            inner.append(nums[j])
            self.dfs(nums, j + 1, inner, result)
            inner.pop()
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, 0, [], result)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.subsets(nums))
