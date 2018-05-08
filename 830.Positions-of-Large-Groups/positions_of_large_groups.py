# 830. Positions of Large Groups
# https://leetcode.com/problems/positions-of-large-groups/description/


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        ch = ''
        start, end = -1, -1
        result = list()
        cnt = 1

        S += '@'

        for idx, ss in enumerate(S):
            if ss == ch:
                cnt += 1
                end += 1
            else:
                if cnt >= 3:
                    result.append([start, end])
                start = idx
                end = start
                ch = ss
                cnt = 1

        return result
