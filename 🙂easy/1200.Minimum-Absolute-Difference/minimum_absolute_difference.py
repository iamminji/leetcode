# 1200. Minimum Absolute Difference
# https://leetcode.com/problems/minimum-absolute-difference/

from typing import List
from collections import defaultdict


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        d = defaultdict(list)
        m = abs(arr[1] - arr[0])
        d[m].append([arr[0], arr[1]])
        for i in range(2, len(arr)):
            val = abs(arr[i] - arr[i - 1])
            d[val].append([arr[i - 1], arr[i]])
            m = min(m, val)
        return d[m]
