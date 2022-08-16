# 1323. Maximum 69 Number
# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number(self, num: int) -> int:

        org = num

        if num // 1000 != 0:
            p = 1000
        elif num // 100 != 0:
            p = 100
        elif num // 10 != 0:
            p = 10
        else:
            p = 1

        r = 0
        while p > 0:
            if num // p == 6:
                return r + 9 * p + num % p
            r += 9 * p
            num %= p
            p //= 10
        return org


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximum69Number(9669))
    print(sol.maximum69Number(9996))
