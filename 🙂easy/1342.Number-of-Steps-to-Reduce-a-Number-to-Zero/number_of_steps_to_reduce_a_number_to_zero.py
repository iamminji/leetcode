# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# 1342. Number of Steps to Reduce a Number to Zero

from typing import List

class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 1
        while num > 1:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            result += 1
        return result
