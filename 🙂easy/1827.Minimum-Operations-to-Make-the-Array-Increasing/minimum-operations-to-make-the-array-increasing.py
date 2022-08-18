# 1827. Minimum Operations to Make the Array Increasing
# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        org = nums[:]
        result = 0
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < nums[i - 1]:
                nums[i] = nums[i - 1] + 1

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                nums[i + 1] = nums[i] + 1

        for i in range(len(nums)):
            result += abs(nums[i] - org[i])

        # for loop 줄이기
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i - 1] + 1:
        #         result += nums[i - 1] + 1 - nums[i]
        #         nums[i] += nums[i - 1] + 1 - nums[i]
        return result



if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations([1, 2, 3, 5, 1]))
    print(sol.minOperations([1, 5, 2, 4, 1]))
    print(sol.minOperations([1, 1, 1]))
