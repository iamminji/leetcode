# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        d = []
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i, c in enumerate(s):
            if c in v:
                d.append(i)

        if len(d) == 0:
            return s

        new_s = list(s)
        i = 0
        d = sorted(d)
        while len(d) > 0:
            if new_s[i] in v:
                j = d.pop()
                new_s[i] = s[j]
            i += 1

        return "".join(new_s)
