from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = list()
        n = 1
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i] + n
            p, q = num // 10, num % 10
            result.append(q)
            n = p

        if n != 0:
            result.append(n)

        return result[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([1, 2, 3, 4]))
    print(sol.plusOne([1, 2, 3, 9]))
