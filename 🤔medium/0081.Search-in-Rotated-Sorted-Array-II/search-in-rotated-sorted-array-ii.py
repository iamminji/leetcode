# 81. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        start, end = 0, len(nums) - 1

        while start <= end:

            while start < end and nums[start] == nums[start + 1]:
                if nums[start] == target:
                    return True
                start += 1

            while start < end and nums[end] == nums[end - 1]:
                if nums[end] == target:
                    return True
                end -= 1

            mid = (start + end) // 2

            if nums[mid] == target:
                return True

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.search([1, 0, 1, 1, 1], 0))
    print(sol.search([2, 5, 6, 0, 0, 1, 2], 3))
    print(sol.search([1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13))
    print(sol.search([6, 1, 2, 4, 5], 1))
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(sol.search([1, 3, 5], 1))
