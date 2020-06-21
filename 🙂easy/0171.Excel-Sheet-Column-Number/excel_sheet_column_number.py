# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/


class Solution:
    def titleToNumber(self, s: str) -> int:
        m = {}

        for i in range(1, 27):
            m[chr(i + 64)] = i

        res = 0

        for c in s:
            res = 26 * res + m[c]

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.titleToNumber("AAA"))
    print(sol.titleToNumber("AA"))
    print(sol.titleToNumber("A"))
    print(sol.titleToNumber("AB"))
    print(sol.titleToNumber("ZY"))
