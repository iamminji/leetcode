# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n

        dp = [0 for _ in range(n + 1)]

        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(5))
    print(sol.climbStairs(4))
    print(sol.climbStairs(12))
