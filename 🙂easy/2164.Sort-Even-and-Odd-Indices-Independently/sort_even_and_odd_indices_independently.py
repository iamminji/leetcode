# 2164. Sort Even and Odd Indices Independently
# https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_nums = []
        odd_nums = []

        for i in range(len(nums)):
            if i % 2 == 0:
                even_nums.append(nums[i])
            else:
                odd_nums.append(nums[i])

        even_nums.sort()
        odd_nums.sort(reverse=True)

        i, j = 0, 0
        k = 0
        result = [0 for _ in range(len(nums))]
        while i < len(even_nums):
            result[k] = even_nums[i]
            i += 1
            k += 2

        k = 1
        while j < len(odd_nums):
            result[k] = odd_nums[j]
            j += 1
            k += 2
        return result
