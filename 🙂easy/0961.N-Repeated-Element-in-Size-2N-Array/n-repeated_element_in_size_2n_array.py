# 961. N-Repeated Element in Size 2N Array
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

from typing import List

class Solution:
    # 반복되는 수를 리턴하는 문제다.
    def repeatedNTimes(self, A: List[int]) -> int:
        s = set()
        for num in A:
            if num not in s:
                s.add(num)
            else:
                return num
        return 0
