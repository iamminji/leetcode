# 263. Ugly Number
# https://leetcode.com/problems/ugly-number/


class Solution:

    def isUgly(self, num: int) -> bool:

        if num == 0:
            return False
        skip = False
        while num != 1:
            if skip:
                return False
            do = False
            if num % 2 == 0:
                do = True
                num /= 2
            if num % 3 == 0:
                do = True
                num /= 3
            if num % 5 == 0:
                do = True
                num /= 5

            if not do:
                skip = True
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isUgly(14))
    print(sol.isUgly(8))
