# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        p = list(pattern)
        s = str.split(" ")

        d1 = {}
        d2 = {}
        if len(p) != len(s):
            return False
        for a, b in zip(p, s):
            if a not in d1 and b not in d2:
                d1[a] = b
                d2[b] = a
            else:
                if a not in d1 and b in d2:
                    return False
                if a in d1 and b not in d2:
                    return False
                if d1[a] != b or d2[b] != a:
                    return False

        return True
