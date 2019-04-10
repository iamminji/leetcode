# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotateTLE(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums[0], nums[1:len(nums)] = nums[len(nums) - 1], nums[:len(nums) - 1]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    sol = Solution()
    print(sol.rotate([1, 2, 3, 4, 5, 6, 7, 8], 4))
    print(sol.rotate([1, 2, 3, 4, 5], 3))
