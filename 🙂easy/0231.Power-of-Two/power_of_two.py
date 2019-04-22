# 231. Power of Two
# https://leetcode.com/problems/power-of-two/


class Solution:
    # 2의 제곱근이 맞는지 리턴하는 문제다.
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        # bit count 를 한다.
        # 2의 제곱근은 1이 하나밖에 없다.
        return bin(n).count("1") == 1

    def isPowerOfTwo2(self, n: int) -> bool:
        if n < 0:
            return False
        # 어째서인지 예전에 외웠었음
        return (n & n - 1) == 0
