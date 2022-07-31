# https://leetcode.com/contest/weekly-contest-304/problems/maximum-number-of-groups-entering-a-competition/
from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        result = 1
        pos = 2
        s = 1
        while s + pos <= len(grades):
            s, pos = s + pos, pos + 1
            result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumGroups([10, 6, 12, 7, 3, 5]))
    print(solution.maximumGroups([2, 31, 41, 31, 36, 46, 33, 45, 47, 8, 31, 6, 12, 12, 15, 35]))
    print(solution.maximumGroups([8, 8]))
