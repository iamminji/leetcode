# 1486. XOR Operation in an Array
# https://leetcode.com/problems/xor-operation-in-an-array/description/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        r = start
        i = 1
        while i < n:
            r = r ^ (start + 2 * i)
            i += 1
        return r
