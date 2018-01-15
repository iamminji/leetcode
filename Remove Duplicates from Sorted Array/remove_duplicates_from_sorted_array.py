# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return len(nums)

        point = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[point] = nums[i]
                point += 1

        return point
