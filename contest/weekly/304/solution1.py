# https://leetcode.com/contest/weekly-contest-304/problems/make-array-zero-by-subtracting-equal-amounts/
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        while True:
            sub = max(nums)
            if sub == 0:
                break
            result += 1
            for num in nums:
                if num > 0:
                    sub = min(num, sub)
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] -= sub
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumOperations([1, 5, 0, 3, 5]))
    print(solution.minimumOperations([1, 1, 0, 2, 1]))
    print(solution.minimumOperations([]))
