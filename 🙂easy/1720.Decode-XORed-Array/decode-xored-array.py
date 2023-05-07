# 1720. Decode XORed Array
# https://leetcode.com/problems/decode-xored-array/description/

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # xor 연산은 한번 더 하면 원래 값이 나온다.
        result = [first]
        i = 1
        for e in encoded:
            result.append(result[i - 1] ^ e)
            i += 1
        return result
