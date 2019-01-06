# 541. Reverse String II
# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return "".join(s)
