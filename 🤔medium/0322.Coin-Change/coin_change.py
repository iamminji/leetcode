# 322. Coin Change
# https://leetcode.com/problems/coin-change/


class Solution:

    # amount 를 만들 수 있는 최소한의 coin 개수를 리턴하는 문제다.
    # 전형적인 dp 문제다.
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':

        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        # coin 이 amount 라면 최소한의 동전 개수는 1이므로 아래처럼 업데이트 해준다.
        for coin in coins:
            if coin > amount:
                continue
            dp[coin] = 1

        # 4원을 만드는데 필요한 동전의 최소 개수는
        # 3원을 만드는데 필요한 최소한의 개수 + 1원을 만드는데 필요한 최소한의 개수, 2원을 만드는데 필요한 최소한의 개수 * 2 ... 이다.
        # 식으로 표현하면 아래와 같다.

        # dp[4] = min(dp[3] + dp[1], dp[2] + dp[2] ... )
        # dp[x] = min(dp[x-i] + dp[i], dp[x-i-1] + dp[i+1] ...)

        # i 를 0 ~ x 로 하면 TLE 가 나오기 떄문에, 어차피 사용하는 돈은 주어진 coins 이므로 i 대신에 coin 으로 바꿔주고
        # 동전이 구하고자 하는 amount 보다 크면 의미가 없으므로 넘어가면 된다.
        for x in range(amount + 1):
            for coin in coins:
                if coin > x:
                    continue
                dp[x] = min(dp[x - coin] + dp[coin], dp[x])

        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == '__main__':
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([1, 2], 4) == 2
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 1) == 1
    assert sol.coinChange([2], 2) == 1
    assert sol.coinChange([1], 0) == 0
    assert sol.coinChange([1, 2147483647], 2) == 2
    assert sol.coinChange([431, 62, 88, 428], 9084) == 26
