# 1979. Find Greatest Common Divisor of Array
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

from typing import List


class Solution:

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def findGCD(self, nums: List[int]) -> int:
        # gcd(a,b) = gcd(b, a%b) (a>b, b!=0)
        minnum = min(nums)
        maxnum = max(nums)

        return self.gcd(maxnum, minnum)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findGCD([2, 5, 6, 9, 10]))
    print(solution.findGCD([7, 5, 6, 8, 3]))
    print(solution.findGCD([3, 3]))
