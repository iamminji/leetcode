# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/

from typing import List


class Solution:
    def recursive(self, nums, start, end):
        if end - start == 1:
            if nums[start] < nums[end]:
                return end
            return start

        mid = (start + end) // 2

        left = self.recursive(nums, start, mid)
        right = self.recursive(nums, mid, end)

        if nums[left] < nums[right]:
            return right
        return left

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        return self.recursive(nums, 0, len(nums) - 1)

    def findPeakElementWithLinear(self, nums: List[int]) -> int:

        i = 0
        k = 0
        mx = -1
        mxi = 0

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            if nums[0] < nums[1]:
                return 1
            return 0

        while i < len(nums) - 2:
            if nums[i] < nums[i + 1] and nums[i + 2] < nums[i + 1]:
                return i + 1
            k = nums[i + 1] - nums[i]
            if nums[i] > mx:
                mx = nums[i]
                mxi = i
            i += 1

        if k > 0:
            if nums[i] < nums[i + 1]:
                return i + 1
            return i
        else:
            return mxi


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeakElement([1, 2, 3, 1]))
    print(sol.findPeakElement([4, 3, 2, 1]))
    print(sol.findPeakElement([1, 2, 3, 4]))
    print(sol.findPeakElement([1, 2, 3, 4, 5, 6, 4]))
    print(sol.findPeakElement([3, 2, 5, 5, 3, 1, 2, 3]))
