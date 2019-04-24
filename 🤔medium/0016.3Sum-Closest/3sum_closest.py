# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

from typing import List


class Solution:
    # nums 에서 세 가지 수를 조합하여 target과 가장 가까운 세 수의 합산을 리턴하는 문제다.
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        snums = sorted(nums)
        res = snums[0] + snums[1] + snums[len(snums) - 1]
        for i in range(len(snums)):
            start = i + 1
            end = len(snums) - 1
            while start < end:
                s = snums[i] + snums[start] + snums[end]
                if s == target:
                    return target
                elif s < target:
                    if abs(target - res) > abs(target - s):
                        res = s
                    start += 1
                else:
                    if abs(target - res) > abs(target - s):
                        res = s
                    end -= 1

        return res
