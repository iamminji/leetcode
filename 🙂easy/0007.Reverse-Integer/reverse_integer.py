# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/


class Solution:
    # 주어진 integer 를 reverse 하는 문제다.
    # 단, 일정 범위를 벗어나면 0으로 리턴한다.
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        # - 기호가 있는 경우 확인
        n, s = (1, str(x)) if x > 0 else (-1, str(x)[1:])
        r = int(s[::-1]) * n
        # 일정 범위를 벗어나면 0 을 리턴 아닌 경우엔
        # 주어진 수 x를 문자열로 바꾸고 reverse 한 (그리고 음수일 경우 -를 곱하여) int 를 리턴
        return r if pow(-2, 31) < r <= pow(2, 31) else 0


if __name__ == '__main__':
    # 최대한 짧고, pythonic 하게 하려고 했지만
    # 범위를 벗어나면 0을 리턴해야 하는 것을 몰라서 엄청난 양의 WA가 떴다.
    # 문제를 제대로 읽자. 흑흑
    # downvote도 살포시 눌러줬다.
    sol = Solution()
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
    assert sol.reverse(120) == 21
    assert sol.reverse(1534236469) == 0
