# 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/

from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return (A == sorted(A)) or (A == sorted(A, reverse=True))
