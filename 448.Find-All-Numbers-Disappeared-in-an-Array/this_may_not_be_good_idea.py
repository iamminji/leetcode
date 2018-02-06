# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


# for specific size array, this solution may not be good idea


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = list()

        for _ in range(5):
            for idx in range(len(nums)):
                if idx + 1 != nums[idx]:
                    key = nums[idx]
                    if key != nums[key - 1]:
                        nums[idx], nums[key - 1] = nums[key - 1], nums[idx]

        for idx in range(len(nums)):
            if idx + 1 != nums[idx]:
                res.append(idx + 1)

        return res
