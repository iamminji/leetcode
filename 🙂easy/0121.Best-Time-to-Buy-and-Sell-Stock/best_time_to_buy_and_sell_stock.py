# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


from typing import List


class Solution:
    # prices 라는 integer list 가 들어올 때 가장 적은 가격에 사서 비싸게 팔 때 생기는 이익을 리턴하는 문제다.
    def maxProfit(self, prices: List[int]) -> int:

        # 최소 금액 buy 와 현재 금액 - buy 의 값의 maximum 을 구하면 된다.
        # 왜냐하면 가장 적은 가격에 사서 (min) 가장 비싸게 팔아야 (max) 하기 때문이다.
        # greedy 로 생각해서 하면 된다.

        buy = float("inf")
        res = 0
        for price in prices:
            # 최소 금액 갱신
            buy = min(buy, price)
            # 판매 최대 이익
            res = max(res, price - buy)

        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
