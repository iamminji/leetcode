# 693. Binary Number with Alternating Bits
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        bits = bin(n)[2:]

        for i in range(len(bits) - 1):
            if bits[i] == bits[i + 1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasAlternatingBits(5))
    print(sol.hasAlternatingBits(7))
