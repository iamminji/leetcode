# 2160. Minimum Sum of Four Digit Number After Splitting Digits
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/


class Solution:

    def minimumSum(self, num: int) -> int:
        nums = []
        p = 1000
        while p > 0:
            nums.append(num // p)
            num = num % p
            p //= 10
        nums.sort()

        return nums[0] * 10 + nums[2] + nums[1] * 10 + nums[3]