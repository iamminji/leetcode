# https://leetcode.com/contest/weekly-contest-278/problems/all-divisions-with-the-highest-score-of-a-binary-array/

from collections import defaultdict


class Solution(object):

    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = defaultdict(list)

        lc = 0
        rc = 0
        for num in nums:
            if num == 1:
                rc += 1
        mx = rc
        result[rc].append(0)

        for i in range(len(nums)):
            if nums[i] == 0:
                lc += 1
            else:
                rc -= 1
            mx = max(lc + rc, mx)
            result[lc + rc].append(i + 1)

        return result[mx]


