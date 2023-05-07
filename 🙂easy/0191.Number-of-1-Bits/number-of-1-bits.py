# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        count = 0
        while i < 32:
            if n & 1 == 1:
                count += 1
            n = n >> 1
            i += 1
        return count
