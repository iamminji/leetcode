# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    def convertToTitle(self, n: int) -> str:
        m = {}

        for i in range(1, 27):
            m[i] = chr(i + 64)

        res = []

        while n > 0:
            p = (n - 1) // 26
            q = n % 26
            if q != 0:
                res.append(m[q])
            else:
                res.append('Z')
            n = p

        return "".join(res[::-1])


if __name__ == '__main__':
    sol = Solution()
    # print(sol.convertToTitle(1))
    # print(sol.convertToTitle(27))
    # print(sol.convertToTitle(26 * 26 + 27))
    print(sol.convertToTitle(701))
    # print(sol.convertToTitle(10214))
    # print(sol.convertToTitle(52))
