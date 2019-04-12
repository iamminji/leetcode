# 500. Keyboard Row
# https://leetcode.com/problems/keyboard-row/


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d1 = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
        d2 = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
        d3 = {"z", "x", "c", "v", "b", "n", "m"}

        res = []
        for word in words:
            s = set(word.lower())
            if len(s - d1) == 0 or len(s - d2) == 0 or len(s - d3) == 0:
                res.append(word)
        return res
