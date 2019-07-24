# 1122. Relative Sort Array
# https://leetcode.com/problems/relative-sort-array/


from collections import defaultdict
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # arr2 를 키로 삼아서, arr1 을 정렬하는 문제이다.
        # arr1 의 원소를 카운팅 해 준 후, arr2 순서 대로 카운팅한 개수 만큼 값을 만들어준다.
        # 사용한 키(값)는 제거해준다.
        # 그리고 남은 키(값) 들에 대하여 정렬 (s_count) 을 진행한 후 다시 그 키의 개수 만큼 반복해서 값에 더해준다.

        count = defaultdict(int)
        for i in range(len(arr1)):
            count[arr1[i]] += 1

        res = []
        for k in arr2:
            j = 0
            while j < count[k]:
                res.append(k)
                j += 1
            del count[k]

        s_count = sorted(count)
        for k in s_count:
            j = 0
            while j < count[k]:
                res.append(k)
                j += 1

        return res
