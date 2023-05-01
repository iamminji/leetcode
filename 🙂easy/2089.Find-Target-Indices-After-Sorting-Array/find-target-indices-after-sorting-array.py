# 2089. Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        m_cnt = 0
        t_cnt = 0

        for num in nums:
            if num < target:
                m_cnt += 1
            if num == target:
                t_cnt += 1

        result = []
        for i in range(t_cnt):
            result.append(m_cnt + i)

        return result
