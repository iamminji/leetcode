# 767. Reorganize String
# https://leetcode.com/problems/reorganize-string/description/

from collections import Counter
from heapq import heappop, heappush


class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        counter = Counter(S)
        heap = list()
        for s, c in counter.items():
            heappush(heap, (-1 * c, s))

        res = list()
        while len(heap) >= 2:
            c1, s1 = heappop(heap)
            c2, s2 = heappop(heap)

            if not res or res[-1] != s1:
                res.append(s1)
                res.append(s2)
                if c1 + 1 < 0:
                    heappush(heap, (c1 + 1, s1))
                if c2 + 1 < 0:
                    heappush(heap, (c2 + 1, s2))

        if heap:
            c, s = heappop(heap)
            if abs(c) != -1:
                return ""
            res.append(s)

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.reorganizeString("aab"))
    # print(sol.reorganizeString("abcbc"))
    print(sol.reorganizeString("bbbbaaaaaaacc"))
    print(sol.reorganizeString("aaab"))
    print(sol.reorganizeString("vvvlo"))
