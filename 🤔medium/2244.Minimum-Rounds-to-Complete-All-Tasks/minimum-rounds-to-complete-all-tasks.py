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
                # +1 을 해주는 이유는
                # 3으로 나누어 떨어지지 않는 경우 3K + 1, 3K + 2 가 있다.
                # 3K + 2 는 3K + 2 * 1 과 같음 ==> 따라서 K + 1
                # 3K + 1 은 3(K-1) + 4 = 3(K-1) + 2 * 2 와 같음 ==> K - 1 + 2 ==> K + 1
                # K 가 어떤 값이든 + 1 을 해주면 됨
                res += count // 3 + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumRounds([1 for _ in range(16)]))
