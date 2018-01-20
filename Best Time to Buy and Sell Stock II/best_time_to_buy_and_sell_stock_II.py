# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        result = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                result += (prices[i] - prices[i - 1])
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1, 4, 2]))
    print(sol.maxProfit([2, 1, 2, 0, 1]))
