# 2244. Minimum Rounds to Complete All Tasks
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        t = Counter(tasks)
        res = 0
        for _, count in t.items():
            if count == 1:
                return -1
            if count % 3 == 0:
                res += count // 3
            else:
                res += count // 3 + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumRounds([1 for _ in range(16)]))
