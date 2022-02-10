# https://leetcode.com/contest/biweekly-contest-71/problems/minimum-difference-in-sums-after-removal-of-elements/

from typing import List
from heapq import heappop, heappush


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # sum(first) 이 작을수록 / sum(second) 클수록 좋음
        # 이렇게 되려면
        # 첫번째 배열에서 가장 큰 값을 제거해야 하고
        # 두번째 배열에서는 가장 작은 값을 없애면 된다.

        # 값 제거를 위해 heap (priority queue) 을 사용

        size = len(nums) // 3

        first = []
        first_min_sum = 0
        second = []
        second_max_sum = 0
        temp = [0 for _ in range(len(nums))]

        # 배열 길이 // 3 만큼 pick 해야 함

        # 그래서 len(nums) - size 이상은 선택할 수 없음
        # 해당 값은 second 에 (최소한!) 들어가야 하기 때문
        for i in range(len(nums) - size):
            # python 에서 heap 은 minheap 이라 -1 을 곱해주는 것이다.
            heappush(first, -nums[i])
            first_min_sum += nums[i]
            if len(first) > size:
                n = heappop(first)
                first_min_sum -= -n
            if len(first) == size:
                # 현재 최소값을 담음
                temp[i] = first_min_sum

        result = float("inf")
        for i in range(len(nums) - 1, size - 1, -1):
            heappush(second, nums[i])
            second_max_sum += nums[i]
            if len(second) > size:
                n = heappop(second)
                second_max_sum -= n
            if len(second) == size:
                temp[i] = temp[i - 1] - second_max_sum
                result = min(result, temp[i])

        return result


if __name__ == '__main__':
    sol = Solution()
    # print(sol.minimumDifference([8, 1, 3, 7, 9, 5]) == -12)
    # print(sol.minimumDifference([7, 9, 5, 8, 1, 3]) == 1)
    print(sol.minimumDifference([1, 2, 3, 5, 6, 5, 4, 3, 2]))
