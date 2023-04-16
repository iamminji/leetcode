# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1

        pos = [10 ** 9 + 1, -(10 ** 9) - 1]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                pos[0] = min(pos[0], mid)
                pos[1] = max(pos[1], mid)
                start += 1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                pos[0] = min(pos[0], mid)
                pos[1] = max(pos[1], mid)
                end -= 1

        if pos == [10 ** 9 + 1, -(10 ** 9) - 1]:
            return [-1, -1]
        return pos
