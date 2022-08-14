# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        result = 0

        while any(amount):
            amount.sort(reverse=True)
            if amount[0] > 0:
                amount[0] -= 1
            else:
                break
            if amount[1] > 0:
                amount[1] -= 1
            result += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.fillCups([1, 4, 2]))
    print(sol.fillCups([5, 4, 4]))
    print(sol.fillCups([5, 0, 0]))
