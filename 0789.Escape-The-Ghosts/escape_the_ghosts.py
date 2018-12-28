# 789. Escape The Ghosts
# https://leetcode.com/problems/escape-the-ghosts/description/


class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        for g in ghosts:
            dist = abs(g[0] - target[0]) + abs(g[1] - target[1])
            if abs(target[0]) + abs(target[1]) >= dist:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.escapeGhosts([[1, 0], [0, 3]], [0, 1]))
    print(sol.escapeGhosts([[1, 0]], [2, 0]))
