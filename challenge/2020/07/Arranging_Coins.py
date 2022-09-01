from math import sqrt


class Solution:
    def arrangeCoinsWithWhile(self, n: int) -> int:
        a = 1
        b = 2
        while b <= (2 * n):
            a += 1
            b = (pow(a, 2) + a)

        return a - 1

    def arrangeCoinsWithMath(self, n: int) -> int:
        return int(sqrt((2 * n) + 0.25) - 0.5)


if __name__ == '__main__':
    sol = Solution()
    print(sol.arrangeCoinsWithMath(8))
    print(sol.arrangeCoinsWithMath(5))
