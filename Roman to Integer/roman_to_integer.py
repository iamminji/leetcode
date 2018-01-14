# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/

# roman
# https://www.rapidtables.com/convert/number/roman-numerals-converter.html


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = 0
        cache = dict()
        roman = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        for idx in range(0, len(s)):
            if s[idx:idx + 2] in roman:
                result += roman[s[idx:idx + 2]]
                cache[idx] = True

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        idx = 0
        while idx < len(s):
            if idx not in cache:
                result += roman[s[idx:idx + 1]]
                idx += 1
            else:
                idx += 2
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("DCXXI"))
    print(sol.romanToInt("MCMXCVI"))
