# 1128. Number of Equivalent Domino Pairs
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

from typing import List
from collections import defaultdict


class Solution:

    def combination(self, n, r):
        if r <= 1:
            return n
        return self.combination(n - 1, r - 1) * n / r

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 동일한 pair 리스트를 찾는 문제로 서로 인덱스 위치가 달라도 pair 라고 본다.
        # TLE가 떠서, 다음과 같이 줄이는 시도를 했다.
        # 주어진 리스트의 inner pair 리스트의 값으로 정렬하였다.
        #   [[0, 1], [1, 0]] 을 [[0, 1], [0, 1]] 로 바꾸었다.
        # 그리고 pair 일 때만 인덱스 (j) 를 증가시키고 j - i 는 동일하게 등장한 pair 개수와 같다.
        # 전체 개수에서 2개를 고르는 경우의 수가 문제에서 요구하는 pair의 경우의 수 와 같다.
        #   따라서 이 부분에서 combination 함수를 작성하고 값을 더해주었다.

        result = 0

        for domino in dominoes:
            if domino[0] > domino[1]:
                domino[0], domino[1] = domino[1], domino[0]

        dominoes = sorted(dominoes, key=lambda x: (x[0], x[1]))
        i = 0
        while i < len(dominoes):
            j = i + 1
            while j < len(dominoes) and dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
                j += 1
            result += self.combination(j - i, 2)
            i = j

        return int(result)

    def numEquivDominoPairs2(self, dominoes: List[List[int]]) -> int:
        # numEquivDominoPairs 와 동일한 로직을 정리하였다.
        # 사실 정렬까지 할 필요 없고 값은 2개이므로 pair 로 딕셔너리를 만들면 된다.
        # 사실2 combination 함수 까지 구현할 필요 없고 무조건 2개 골라야 하므로 n * (n-1) / 2 를 하면 된다
        d = defaultdict(int)

        for domino in dominoes:
            if domino[0] > domino[1]:
                d[(domino[0], domino[1])] += 1
            else:
                d[(domino[1], domino[0])] += 1

        result = 0
        for _, v in d.items():
            result += (v * (v - 1)) / 2
        return int(result)

    def numEquivDominoPairsTLE(self, dominoes: List[List[int]]) -> int:
        # TLE
        res = 0
        for i in range(len(dominoes)):
            for j in range(i + 1, len(dominoes)):
                if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
                    res += 1
                elif dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]:
                    res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.numEquivDominoPairs2([[1, 2], [2, 1], [3, 4], [5, 6]]))
    print(solution.numEquivDominoPairs2([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
    print(solution.numEquivDominoPairs2([[2, 2], [2, 1], [2, 2], [2, 1], [2, 2], [1, 2], [2, 2], [1, 1], [1, 1]]))
