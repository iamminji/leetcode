# 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/

from typing import List
from collections import defaultdict


class Solution:

    # 주어진 배열 4개의 원소들을 이용해서 합산한 값이 0이 되는 경우의 수를 리턴하는 문제다.
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        t1 = defaultdict(int)
        t2 = defaultdict(int)

        # 배열 두개씩 임의로 묶어서 합산한 값을 키로 쓰고, 각 키에 대한 카운팅을 해 준다.
        for i in A:
            for j in B:
                t1[i + j] += 1

        for k in C:
            for l in D:
                t2[k + l] += 1

        result = 0

        # 카운팅한 딕셔너리에서 키가 서로 반대되는 값이면 값을 곱해준다.
        # 이 이유는 문제에서 원하는 것이 각 배열의 임의의 값들의 합이 0이 되는 것인데, 이미 키에는 배열 원소의 합산이 들어가 있다.
        # 두 딕셔너리가 서로 반대뇌는 원소가 들어있다는 의미는 합하면 0이 된다는 것이다.
        # 즉 (임의로 묶은) A, B 의 원소의 합들과 C, D 의 원소의 합들 중에서 서로 반대뇌는 것들을 찾는다는 의미다.
        # 곱하기를 해 주는 이유는 경우의 수를 구해야 하는 것이기 때문에 곱하기를 해 줬다.
        for k, v in t1.items():
            if -k in t2 and v >= 1 and t2[-k] >= 1:
                result += v * t2[-k]

        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
    assert sol.fourSumCount([1, 1], [-1, -1], [-1, -1], [1, 1]) == 16
