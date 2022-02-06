# https://leetcode.com/contest/biweekly-contest-71/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
class Solution:
    def minimumSum(self, num: int) -> int:
        snums = list(str(num))
        snums.sort()
        return int(snums[0]) * 10 + int(snums[2]) + int(snums[1]) * 10 + int(snums[3])
