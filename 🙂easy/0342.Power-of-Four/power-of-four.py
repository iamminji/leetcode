# 342. Power of Four
# https://leetcode.com/problems/power-of-four/description/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n & (n - 1) != 0:
            return False

        num = int('10101010101010101010101010101010', 2)
        return n & num != n
