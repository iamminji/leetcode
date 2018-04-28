# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/description/


class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        bits = [0, 1, 1, 2, 1, 2]
        if num < 5:
            return bits[:num+1]

        for n in range(6, num + 1):
            res = n & (n - 1)
            if res == 0:
                temp = 1
            else:
                temp = bits[n - res] + bits[res]
            bits.append(temp)

        return bits


if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(5))
    print(sol.countBits(2))
    print(sol.countBits(7))
    print(sol.countBits(6))
    print(sol.countBits(12))
