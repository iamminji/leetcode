# 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/description/

from collections import deque


class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        queue = deque(S)
        res = list()

        while len(queue) > 0:
            item = queue.popleft()
            idx = 0
            while idx < len(T):
                if T[idx] == item:
                    res.append(item)
                    T = T[:idx] + T[idx + 1:]
                else:
                    idx += 1

        if T:
            for ch in T:
                res.append(ch)

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.customSortString('bcd', 'abcdabcd'))
    print(sol.customSortString('cba', 'abcd'))
