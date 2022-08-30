# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = prices[0]
        result = 0
        for i in range(1, len(prices)):
            result = max(prices[i] - cur, result)
            cur = min(prices[i], cur)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
