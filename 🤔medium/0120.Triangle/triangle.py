# 120. Triangle
# https://leetcode.com/problems/triangle/

from typing import List


class Solution(object):
    # triangle 에서 minimum path 를 구하는 문제다.
    # 전형적인 dp 문제다.
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        height = len(triangle)

        if height == 1:
            return min(triangle[0])

        # 현재 값의 최소 값은 바로 위의 (height-1) 값 과 바로 위의 옆에 값 의 최소 값 + 현재 값이다.
        # 가장 끄트머리에 있는 것들만 예외 처리를 해주는 방식(끄트머리의 것들은 바로 위의 것만 영향을 받는다) 으로 top-down 으로 구했다.
        for i in range(1, height):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                    continue
                if j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                    continue
                triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]

        return min(triangle[height - 1])


if __name__ == '__main__':
    sol = Solution()
    assert sol.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]) == 11
