# 229. Majority Element II
# https://leetcode.com/problems/majority-element-ii/description/

from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        counter = Counter(nums)
        return [num for num, count in counter.items() if count > len(nums) / 3]


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([1, 1, 1, 2]))
