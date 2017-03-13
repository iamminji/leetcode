from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_count = defaultdict(lambda: 0)
        t_count = defaultdict(lambda: 0)
        for c in s:
            s_count[c] += 1
        for c in t:
            t_count[c] += 1

        if len(s_count) > len(t_count):
            for c in s_count:
                if t_count[c] != s_count[c]:
                    return False
        else:
            for c in t_count:
                if t_count[c] != s_count[c]:
                    return False
        return True
