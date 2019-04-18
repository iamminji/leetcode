# 670. Maximum Swap
# https://leetcode.com/problems/maximum-swap/
from copy import copy


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        res = copy(nums)

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                if int("".join(nums)) > int("".join(res)):
                    res = copy(nums)
                nums[i], nums[j] = nums[j], nums[i]

        return int("".join(res))


if __name__ == '__main__':
    sol = Solution()
    assert sol.maximumSwap(2736) == 7236
    assert sol.maximumSwap(9973) == 9973
