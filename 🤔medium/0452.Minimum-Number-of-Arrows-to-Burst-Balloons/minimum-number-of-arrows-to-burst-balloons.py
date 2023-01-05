# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # point 값이 최소 1개 이상 있어서
        # 무조건 한개의 화살을 쏘게 되어 있음
        result = 1

        # 풍선의 끝점으로 정렬함
        points.sort(key=lambda x: x[1])
        prev = points[0]
        for point in points:
            # 풍선이 서로 안 닿아 있음
            # 그러면 다음 풍선을 burst 하기 위해 화살을 쏜다
            if prev[1] < point[0]:
                result += 1
                prev = point
            # else 라면 닿아 있다는 의미 이므로
            # 화살을 쏠 필요가 없다. (이미 prev 풍선 확인 하면서 쐈기 때문임)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
