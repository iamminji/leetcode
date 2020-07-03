from typing import List
from copy import copy
from collections import defaultdict


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # cells size is fixed

        result = defaultdict(list)

        for i in range(15):
            result[i] = copy(cells)
            org = copy(cells)
            for j in range(1, 7):
                if org[j - 1] != org[j + 1]:
                    cells[j] = 0
                else:
                    cells[j] = 1

            cells[0] = 0
            cells[7] = 0

        return result[N % 14]


if __name__ == '__main__':
    sol = Solution()

    c1 = [0, 1, 0, 1, 1, 0, 0, 1]
    n1 = 7
    print(sol.prisonAfterNDays(c1, n1), [0, 0, 1, 1, 0, 0, 0, 0])

    c2 = [1, 0, 0, 1, 0, 0, 1, 0]
    n2 = 1000000000
    print(sol.prisonAfterNDays(c2, n2))

    c3 = [1, 0, 0, 1, 0, 0, 0, 1]
    n3 = 826
    print(sol.prisonAfterNDays(c3, n3), [0, 1, 1, 0, 1, 1, 1, 0])
