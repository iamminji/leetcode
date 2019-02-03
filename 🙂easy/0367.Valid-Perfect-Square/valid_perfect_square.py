# 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/


class Solution:

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        i = 1
        k = 1

        while k < num:
            i += 2
            k += i

        return k == num
