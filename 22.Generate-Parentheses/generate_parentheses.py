# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/

from collections import deque


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        queue = deque()
        if n >= 1:
            queue.append(('(', 1, 0))

        result = []
        c = 0
        while len(queue) > 0:
            c += 1
            vp, o_cnt, c_cnt = queue.popleft()
            if c_cnt <= o_cnt <= n:
                queue.append((vp + '(', o_cnt + 1, c_cnt))
                queue.append((vp + ')', o_cnt, c_cnt + 1))

            if o_cnt == c_cnt == n:
                result.append(vp)

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
