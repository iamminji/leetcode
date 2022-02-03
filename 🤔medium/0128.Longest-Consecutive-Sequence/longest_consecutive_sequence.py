# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        result = 1

        s = set()
        for num in nums:
            s.add(num)

        check = set()
        for num in s:
            r = 1
            if num + 1 not in check and num + 1 in s:
                start = num + 1
                while start in s:
                    r += 1
                    result = max(result, r)
                    check.add(start)
                    start += 1

        return result
