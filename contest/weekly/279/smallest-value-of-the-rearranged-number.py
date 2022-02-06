# https://leetcode.com/contest/weekly-contest-279/problems/smallest-value-of-the-rearranged-number/
from collections import defaultdict


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        neg = False
        if num < 0:
            neg = True

        snum = list(str(num))
        d = defaultdict(int)
        for s in snum:
            d[s] += 1

        if neg:
            digit = "9876543210"
        else:
            digit = "0123456789"

        result = []

        i = 0
        while i < len(digit):
            di = digit[i]
            if di == '0' and not result:
                i += 1
                continue

            if d[di] > 0:
                result.append(di)
                d[di] -= 1
                i = 0
            else:
                i += 1

        if neg:
            return -1 * int("".join(result))
        else:
            return int("".join(result))
