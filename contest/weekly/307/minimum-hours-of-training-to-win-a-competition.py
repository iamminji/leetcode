from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        result = 0

        for e in energy:
            if e < initialEnergy:
                initialEnergy -= e
            else:
                e1 = e - initialEnergy + 1
                initialEnergy = e1 + initialEnergy - e
                result += e1

        for e in experience:
            if e < initialExperience:
                initialExperience += e
            else:
                e1 = e - initialExperience + 1
                initialExperience += e1 + e
                result += e1

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.minNumberOfHours(5, 3, [1, 4, 3, 2], [2, 6, 3, 1]))
    print(sol.minNumberOfHours(2, 4, [1], [3]))
    print(sol.minNumberOfHours(1, 1, [1, 1, 1, 1], [1, 1, 1, 50]))
