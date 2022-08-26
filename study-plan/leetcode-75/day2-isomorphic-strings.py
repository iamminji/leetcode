# https://leetcode.com/problems/isomorphic-strings/
# 205. Isomorphic Strings

from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdic = defaultdict()
        tdic = defaultdict()
        if len(s) != len(t):
            return False

        for a, b in zip(s, t):
            sdic[a] = b
            tdic[b] = a

        for a, b in zip(s, t):
            if sdic[a] != b or tdic[b] != a:
                return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))
    print(sol.isIsomorphic("foo", "bar"))
    print(sol.isIsomorphic("paper", "title"))
    print(sol.isIsomorphic("badc", "baba"))
