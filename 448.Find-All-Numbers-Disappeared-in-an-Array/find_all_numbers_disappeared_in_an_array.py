# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDisappearedNumbers([1, 5, 2, 4, 5]))
    print(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(sol.findDisappearedNumbers([7, 7, 8, 8, 6, 6, 5, 4, 3, 2, 1, 12]))
    print(sol.findDisappearedNumbers([3, 1, 2, 4, 5]))
