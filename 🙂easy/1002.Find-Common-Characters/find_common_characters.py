# 1002. Find Common Characters
# https://leetcode.com/problems/find-common-characters/

from typing import List
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # Python 의 Counter는 리스트 원소들의 카운팅 결과의 딕셔너리를 생성
        res = Counter(A[0])
        for a in A:
            # & 연산을 통해 A 리스트에 있는 원소들의 교집합을 찾는다.
            # Counter의 & 연산은 value 값으로 원소의 카운팅 minimum 을 넣는다.
            res &= Counter(a)

        # elements 함수는 각 key를 value 개수 만큼 만드는 이터레이터다.
        # 그래서 결과 값을 list 로 감싸서 사용한다.
        return list(res.elements())


if __name__ == '__main__':
    sol = Solution()
    assert sorted(sol.commonChars(["bella", "label", "roller"])) == ["e", "l", "l"]
    assert sorted(sol.commonChars(["cool", "lock", "cook"])) == ["c", "o"]
    assert sorted(sol.commonChars(["cook", "lock", "k", "k", "k"])) == ["k"]
    assert sorted(sol.commonChars(["cook"])) == ["c", "k", "o", "o"]
