# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/


class Solution:
    def numSquares(self, n: int) -> int:
        # TLE

        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return int(dp[n])


if __name__ == '__main__':
    sol = Solution()
    assert sol.numSquares(12) == 3
    assert sol.numSquares(13) == 2
