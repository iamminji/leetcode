# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    # 문제 조건이 O(logn) 이기 때문에 Binary Search 관련 문제라는 것을 알 수 있다. (+ 이미 정렬된 nums)
    def searchInsert(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid

        # target 이 들어갈 포지션은 이전 값 보다 크고 다음 값 보다 작은 곳이다.
        # while 문 벗어났다는 건 start > end 라는 의미다.
        # 따라서 이 포지션 값은 start 와 같다
        return start
