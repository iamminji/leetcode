# 799. Champagne Tower
# https://leetcode.com/problems/champagne-tower/description/


class Solution(object):

    def refill(self, cur):
        return cur - 1 if cur > 1 else 0

    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """

        size = 100
        dp = [[0 for _ in range(size)] for _ in range(size)]
        dp[0][0] = poured
        for c in range(1, size):
            for r in range(c + 1):
                if r == 0:
                    dp[c][r] = self.refill(dp[c - 1][r]) * 0.5
                    continue
                dp[c][r] = self.refill(dp[c - 1][r]) * 0.5 + self.refill(dp[c - 1][r - 1]) * 0.5

        return dp[query_row][query_glass] if dp[query_row][query_glass] < 1 else 1


if __name__ == "__main__":
    sol = Solution()
    print sol.champagneTower(6, 3, 2)
