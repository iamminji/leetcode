# 581. Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        sorted_nums = sorted(nums)
        while start < len(nums):
            if nums[start] != sorted_nums[start]:
                break
            start += 1

        end = len(nums) - 1
        while end > start:
            if nums[end] != sorted_nums[end]:
                break
            end -= 1

        return end - start + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(sol.findUnsortedSubarray([1, 2, 3, 4]))
    print(sol.findUnsortedSubarray([2, 1, 1, 3, 4]))
    print(sol.findUnsortedSubarray([4, 3, 2, 1]))
    print(sol.findUnsortedSubarray([1, 3, 2, 3, 3]))
    print(sol.findUnsortedSubarray([1, 3, 2, 4, 5]))
