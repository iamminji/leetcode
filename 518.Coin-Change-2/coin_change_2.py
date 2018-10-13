# 518. Coin Change 2
# https://leetcode.com/problems/coin-change-2/#/description


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for idx in range(coin, amount + 1):
                if coin <= idx:
                    dp[idx] += dp[idx - coin]

        return dp[amount]


if __name__ == "__main__":
    sol = Solution()
    print(sol.change(5, [1, 2, 5]))
