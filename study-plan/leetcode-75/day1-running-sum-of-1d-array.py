# https://leetcode.com/problems/running-sum-of-1d-array/
# 1480. Running Sum of 1d Array
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums