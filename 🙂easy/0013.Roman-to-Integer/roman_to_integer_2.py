# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        i = 0
        result =  0

        while i < len(s) - 1:
            c = s[i]
            if c == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                result += d[s[i+1]] - 1
                i += 2
                continue
            elif c == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                result += d[s[i+1]] - 10
                i += 2
                continue
            elif c == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                result += d[s[i+1]] - 100
                i += 2
                continue
            result += d[c]
            i += 1
        
        if i <= len(s) - 1:
            result += d[s[i]]
        return result
