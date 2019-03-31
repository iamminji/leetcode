# 599. Minimum Index Sum of Two Lists
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

from typing import List
from collections import defaultdict


class Solution:
    # 레스토랑 이름 리스트 2개가 주어지고 여기서 겹치는 레스토랑이 있을 경우 리턴하는 문제다.
    # 단, 겹치는 레스토랑이 여러개라면 해당 레스토랑이 등장하는 인덱스의 최소 합이 가장 적은 것을 리턴해야 하며,
    # 이 최소 합 마저 겹친 다면 겹치는(최소 인덱스 합이 같은) 모든 레스토랑을 리턴하면 된다.

    def findRestaurant2(self, list1: List[str], list2: List[str]) -> List[str]:
        # time Complexity O(N^2)
        i, j = 0, 0
        res = []
        index = []

        while i < len(list1):
            j = 0
            while j < len(list2):
                if list1[i] == list2[j]:
                    res.append(list2[j])
                    index.append(i + j)
                    break
                j += 1
            i += 1

        if len(res) == 0:
            return res

        k = 1
        while k < len(index):
            if index[k - 1] == index[k]:
                k += 1
            else:
                break

        return res[:k]

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # 가장 처음엔 O(N*M) 으로 모든 리스트를 순회하며 구했고 이 역시 AC가 뜨긴 한다(findRestaurant2).
        # 그러나 다시 딕셔너리로 고쳐서 풀었다.
        # 키는 레스토랑 이름을, 값에는 현재 인덱스를 넣고 인덱스를 키로 한 또 다른 딕셔너리(t)를 만들어서 구했다.
        # O(N^2) 에서 O(N) 으로 시간 복잡도를 절약할 수 있었다.
        d = defaultdict(int)
        for i, s in enumerate(list1):
            d[s] = i

        t = defaultdict(list)
        for j, s in enumerate(list2):
            if s in d:
                t[j + d[s]].append(s)

        return t[min(t.keys())]
