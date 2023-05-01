# 852. Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
                return mid
            if arr[mid-1] < arr[mid]:
                start = mid
            else:
                end  = mid
        return 0


if __name__ == '__main__':
    sol = Solution()
    # print(sol.peakIndexInMountainArray([3, 4, 5, 1]))
    # print(sol.peakIndexInMountainArray([3, 5, 3, 2, 0]))
    print(sol.peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
    print(sol.peakIndexInMountainArray([8, 18, 24, 31, 37, 42, 43, 56, 65, 73, 93, 98, 100, 98, 76, 72, 69, 24, 23]))
