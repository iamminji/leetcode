# 231. Power of Two
# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        r, i = 1, 0
        while i <= 32:
            if n ^ r == 0:
                return True
            r = r << 1
            i += 1
        return False
