# https://leetcode.com/problems/binary-search/
# 704. Binary Search
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left += 1
            elif nums[mid] > target:
                right -= 1
            else:
                return mid

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))
