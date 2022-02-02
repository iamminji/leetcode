# https://leetcode.com/contest/weekly-contest-278/problems/keep-multiplying-found-values-by-two/


class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """

        num_set = set()
        found = False

        for num in nums:
            num_set.add(num)
            if num == original:
                found = True

        if not found:
            return original

        o2 = original * 2
        while o2 in num_set:
            o2 = o2 * 2
        return o2
