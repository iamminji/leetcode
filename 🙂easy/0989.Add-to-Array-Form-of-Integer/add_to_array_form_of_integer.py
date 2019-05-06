# 989. Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer/

from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num = int("".join([str(_) for _ in A]))
        return [int(_) for _ in list(str(num + K))]
