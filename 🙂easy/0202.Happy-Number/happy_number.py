# 202. Happy Number
# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:

        skip = set()
        while n > 1:
            res = 0
            for c in str(n):
                res += pow(int(c), 2)
            if res in skip:
                break
            skip.add(res)
            n = res

        return n == 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.isHappy(19))
    print(sol.isHappy(2))
