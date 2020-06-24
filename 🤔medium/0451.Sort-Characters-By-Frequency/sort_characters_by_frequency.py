# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

from heapq import heappop, heappush
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        counter = Counter(s)
        for item in s:
            heappush(heap, (-1 * counter.get(item), item))

        res = ""
        while heap:
            item = heappop(heap)
            res += item[1]

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.frequencySort("tree"))
    print(sol.frequencySort("cccaaa"))
    print(sol.frequencySort("Aabb"))
