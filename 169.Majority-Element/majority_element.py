# 169. Majority Element
# https://leetcode.com/problems/majority-element/description/

from collections import Counter


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = Counter(nums)
        total = len(nums)
        for num in counter:
            if total / 2 < counter[num]:
                return num


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))
