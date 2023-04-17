# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:  # 찾는 값이 우측에 있을 때
                # start 값이 mid 보다 크다면 rotation 되었다.
                # 찾는 값이 end 보다 크다면 우측에 target 없음. 이 값은 rotation 되었기 때문에 좌측에 있다.
                if nums[start] > nums[mid] and nums[end] < target:
                    end = mid - 1
                else:
                    # 일반적인 Binary Search 다.start 값을 증가시킨다.
                    start = mid + 1
            else: # 찾는 값이 왼쪽에 있을 때
                # mid 값이 end 보다 크다면 rotation 되었다.
                # 찾는 값이 start 보다 작다면 좌측에 없음. 이 값은 rotation 되었기 때문에 우측에 있다.
                if nums[mid] > nums[end] and nums[start] > target:
                    start = mid + 1
                else:
                    # 일반적인 Binary Search 다. end 값을 감소시킨다.
                    end = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4, 5, 6, 7, 0, 1, 2, 3], 0))
    print(sol.search([3, 5, 1], 3))
    print(sol.search([5, 6, 7, 1, 2, 3, 4], 5))
