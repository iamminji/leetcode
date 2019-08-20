# 1014. Best Sightseeing Pair
# https://leetcode.com/problems/best-sightseeing-pair/

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        cur, res = 0, 0
        for num in A:
            res = max(res, cur + num)
            # 현재값과 이전에 최대값 비교
            # -1 을 해주는 이유는 진행하면서 거리가 1 만큼 줄어들기 때문
            cur = max(cur, num) - 1
        return res


if __name__ == '__main__':
    sol = Solution()
    # assert sol.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
    assert sol.maxScoreSightseeingPair([10, 9, 8, 100, 2]) == 107
