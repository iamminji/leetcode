# 890. Find and Replace Pattern
# https://leetcode.com/problems/find-and-replace-pattern/

from typing import List
from collections import defaultdict


class Solution:
    # pattern 에 맞는 word 를 찾아 리스트로 리턴하는 문제다.
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        # 딕셔너리 2개를 이용해서 1:1 매칭 되게 만들어주면 된다.
        res = []
        for word in words:
            d1 = defaultdict(str)
            d2 = defaultdict(str)
            for w, p in zip(word, pattern):
                if w not in d1:
                    d1[w] = p
                if p not in d2:
                    d2[p] = w

                # 1:1 매칭이 안되면 종료
                if d1[w] != p or d2[p] != w:
                    break
            else:
                res.append(word)

        return res
